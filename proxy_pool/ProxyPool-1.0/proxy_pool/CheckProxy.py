from gevent import pool, monkey
monkey.patch_all()
from redis import StrictRedis
import requests
from retrying import retry
from threading import Thread


class CheckProxy(object):
	"""代理ip测试"""
	def __init__(self):
		self.sr = StrictRedis()
		# 创建协程池
		self.pool = pool.Pool(10)

	# @retry(stop_max_attempt_number=3)
	def check_proxy(self, url, ip, proxy_type):
		try:
			proxies = {proxy_type: ip.decode()}
			r = requests.get(url, proxies=proxies, timeout=1)
			self.sr.rpush(proxy_type, ip)
		except:
			pass

	def check_transfer(self, url, proxy_type):
		# 通过代理ip类型proxy_type, 调用不通的测试方法
		num = 0
		max_test_time = self.sr.llen(proxy_type)
		print("Redis中 %s proxy 总数为: %s" % (proxy_type.upper(), max_test_time))
		while num < max_test_time:
			ip = self.sr.lpop(proxy_type)
			# 将任务加入协程池
			self.pool.spawn(self.check_proxy, url, ip, proxy_type)
			num += 1

	def run(self):
		print("---------->正在筛选可用proxy<----------")
		url_http = 'http://2018.ip138.com/ic.asp'
		url_https = 'https://www.ip.cn/' 
		# 创建两个线程分别处理不同代理ip类型的函数
		t1 = Thread(target=self.check_transfer, args=(url_http, 'http',))
		t2 = Thread(target=self.check_transfer, args=(url_https, 'https',))
		t1.start()
		t2.start()
		t1.join()
		t2.join()
		print("当前可用 HTTP Proxy 个数为: %s" % self.sr.llen('http'))
		print("当前可用 HTTPS Proxy 个数为: %s" % self.sr.llen('https'))
		print("-------------->筛选完成<-------------")

if __name__ == "__main__":
	test = CheckProxy()
	test.run()





