from setting import redis_clien
from main import RegularlyCheck
from threading import Thread
import time

class GetOneProxy(object):
	"""从Redis中获取Proxy"""

	def __init__(self):
		self.redis_clien = redis_clien()
		self.check = RegularlyCheck()

	def __redisManage(self, proxy_type):
		proxy_addr = self.redis_clien.rpop(proxy_type)  # 代理ip地址
		self.redis_clien.lpush(proxy_type, proxy_addr)
		return proxy_addr.decode()

	def getOneProxy(self, proxy_type='http'):
		'''从redis数据库中获取一个代理ip地址, 代理ip类型为http和https, 默认为http'''

		if self.redis_clien.llen(proxy_type) > 0:
			return self.__redisManage(proxy_type)
		else:
			print("当前数据库中没有数据")
			Thread(target=self.check.regularlyGetProxy).start()
			time.sleep(1)
			return self.__redisManage(proxy_type)


if __name__ == '__main__':
	proxy = GetOneProxy()
	p = proxy.getOneProxy(proxy_type='http')
	print(p)
