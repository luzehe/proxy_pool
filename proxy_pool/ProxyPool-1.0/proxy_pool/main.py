import CheckProxy, getFreeProxy, setting
import time


class RegularlyCheck(object):
	def __init__(self):
		self.redis_clien = setting.redis_clien()  # redis数据库对象
		self.get_proxies = getFreeProxy.GetProxy()
		self.check_proxies = CheckProxy.CheckProxy()

	def regularlyGetProxy(self):
		# 当前数据库中的proxy小于指定要求的proxy数量时, 开始从网上抓取proxy, 并筛选
		while self.redis_clien.llen('http') < setting.PROXY_REQUIRDE_NUMBER:
			self.get_proxies.run()
			self.check_proxies.run()
			time.sleep(setting.PROXY_UPDATE_TIME)  # proxy更新时间, 默认5分钟

if __name__ == '__main__':
	check = RegularlyCheck()
	check.regularlyGetProxy()


			
