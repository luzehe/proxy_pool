import time, hashlib, re, urllib
import setting
from concurrent.futures import ThreadPoolExecutor
from getHTMLTree import getHTMLTree



class GetProxy(object):
	"""从互联网上获取代理ip地址"""
	def __init__(self):
		self.redis_clien = setting.redis_clien()

	def getProxyFirst(self):
		page_count = 0
		max_request_count = 5
		url = 'http://www.xicidaili.com/nn/'
		while page_count < max_request_count:
			item = {}
			html = getHTMLTree(url)
			tr = html.xpath('//table[@id="ip_list"]//tr[position()>1]')
			for td in tr:
				item['ip'] = td.xpath('./td[2]/text()')[0]
				item['port'] = td.xpath('./td[3]/text()')[0]
				item['proxy_type'] = td.xpath('./td[6]/text()')[0]
				self.save_item(item)
			url = urllib.parse.urljoin(url, html.xpath('//a[text()="下一页 ›"]/@href')[0])
			print(item)
			page_count += 1
			time.sleep(5)

	def getProxySecond(self):
		page_count = 0
		max_request_count = 5
		url = 'http://www.89ip.cn/index_1.html'
		while page_count < max_request_count:
			item = {}
			item2 = {}
			html = getHTMLTree(url)
			tr = html.xpath('//table//tr[position()>1]')
			for td in tr:
				item['ip'] = td.xpath('./td[1]/text()')[0].strip()
				item2['ip'] = td.xpath('./td[1]/text()')[0].strip()
				item['port'] = td.xpath('./td[2]/text()')[0].strip()
				item2['port'] = td.xpath('./td[2]/text()')[0].strip()
				item['proxy_type'] = 'http'
				item2['proxy_type'] = 'https'
				self.save_item(item)
				self.save_item(item2)
			url = urllib.parse.urljoin(url, html.xpath('//a[text()="下一页"]/@href')[0])
			page_count += 1
			time.sleep(3)

	def getProxyThird(self):
		page_count = 0
		max_request_count = 5
		url = 'http://www.66ip.cn/1.html'  # 该网址需要先获取cookies和请求头
		cookies = 'yd_cookie=759e0ce3-7ae4-43c16234f2d88af1acd420f82e419bc1dbf0; _ydclearance=f7b4cdc4c65c4485a371483d-5578-4fb8-afed-b9e994e7e7c9-1542773589; Hm_lvt_1761fabf3c988e7f04bec51acd4073f4=1542680644,1542766393; Hm_lpvt_1761fabf3c988e7f04bec51acd4073f4=1542766393'
		cookies = {s.split('=')[0]: s.split('=')[1] for s in cookies.split('; ')}
		headers = {
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'Accept-Encoding': 'gzip, deflate',
			'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
			'Connection': 'keep-alive',
			'Host': 'www.66ip.cn',
			'Upgrade-Insecure-Requests': '1',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
		}
		while page_count < max_request_count:
			item = {}
			item2 = {}
			html = getHTMLTree(url, headers=headers, cookies=cookies)
			tr = html.xpath('//table//tr[position()>1]')
			for td in tr:
				item['ip'] = td.xpath('./td[1]/text()')[0].strip()
				item2['ip'] = td.xpath('./td[1]/text()')[0].strip()
				item['port'] = td.xpath('./td[2]/text()')[0].strip()
				item2['port'] = td.xpath('./td[2]/text()')[0].strip()
				item['proxy_type'] = 'http'
				item2['proxy_type'] = 'https'
				self.save_item(item)
				self.save_item(item2)
			url = urllib.parse.urljoin(url, html.xpath('//a[text()="»"]/@href')[0])
			page_count += 1
			time.sleep(3)


	def getProxyFourth(self):
		url_list = [
		'http://www.data5u.com/free/index.shtml',
		'http://www.data5u.com/free/gngn/index.shtml',
		'http://www.data5u.com/free/gwgn/index.shtml',
		'http://www.data5u.com/free/gnpt/index.shtml',
		'http://www.data5u.com/free/gwpt/index.shtml'
		]

		item = {}
		for url in url_list:
			html = getHTMLTree(url)
			tr = html.xpath('//ul[@class="l2"]')
			for td in tr:
				item['ip'] = td.xpath('./span[1]//text()')[0].strip()
				item['port'] = td.xpath('./span[2]//text()')[0].strip()
				item['proxy_type'] = td.xpath('./span[4]//text()')[0].strip()
				self.save_item(item)
			time.sleep(3)


	def getProxyFifth(self):
		url = 'http://www.goubanjia.com/'
		item = {}
		item2 = {}
		html = getHTMLTree(url)
		proxy_list = html.xpath('//td[@class="ip"]')
		xpath_str = """.//*[not(contains(@style, 'display: none'))
			and not(contains(@style, 'display:none'))
			and not(contains(@class, 'port'))
			]/text()
		"""
		for each_proxy in proxy_list:
			item['ip'] = ''.join(each_proxy.xpath(xpath_str))
			item2['ip'] = ''.join(each_proxy.xpath(xpath_str))
			item['port'] = each_proxy.xpath(".//span[contains(@class, 'port')]/text()")[0]
			item2['port'] = each_proxy.xpath(".//span[contains(@class, 'port')]/text()")[0]
			item['proxy_type'] = 'http'
			item2['proxy_type'] = 'https'
			self.save_item(item)
			self.save_item(item2)

	def getProxySixth(self):
		url = 'https://www.kuaidaili.com/free/{}/{}/'
		url_list = [url.format(s, i)  for s in ['inha', 'intr'] for i in range(1,6)]
		item = {}
		for url in url_list:
			html = getHTMLTree(url)
			tr = html.xpath('//tr')[1:-1]
			for td in tr:
				item['ip'] = td.xpath('./td[@data-title="IP"]/text()')[0]
				item['port'] = td.xpath('./td[@data-title="PORT"]/text()')[0]
				item['proxy_type'] = td.xpath('./td[@data-title="类型"]/text()')[0]
				self.save_item(item)
		time.sleep(3)

	def getProxySeventh(self):
		url = 'http://www.xsdaili.com/'
		html = getHTMLTree(url)
		url_list = html.xpath('//div[@class="title"]/a/@href')[0:2]
		item = {}
		for url in url_list:
			html = getHTMLTree('http://www.xsdaili.com' + url)
			content = html.xpath('//div[@class="cont"]//text()')
			proxies_list = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}@.{4,5}#', str(content), re.S)
			for proxy in proxies_list:
				res = re.match('(.*):(.*)@(.*)#', proxy)
				item['ip'] = res.group(1)
				item['port'] = res.group(2)
				item['proxy_type'] = res.group(3)
				self.save_item(item)

	def save_item(self, item):
		# 通过hashlib.md5, 给每个代理ip生成一个固定的指纹
		md5 = hashlib.md5((item['ip'] + ':' + item['port']).encode())
		fingerprint = md5.hexdigest() 
		# 当指纹不存在时返回1, 反之返回0 
		result = self.redis_clien.sadd('%s_fingerprint' % item['proxy_type'].lower(), fingerprint)
		if result == 1: 
			self.redis_clien.lpush(item['proxy_type'].lower(), item['ip'] + ':' + item['port'])
		

	def run(self):
		try:
			print("------->正在从网上抓取proxy<-------")
			with ThreadPoolExecutor(max_workers=5) as executor:
				executor.submit(self.getProxyFirst)
				executor.submit(self.getProxySecond)
				executor.submit(self.getProxyThird)
				executor.submit(self.getProxyFourth)
				executor.submit(self.getProxyFifth)
				executor.submit(self.getProxySixth)
				executor.submit(self.getProxySeventh)
			print("------------>抓取完成<------------")
		except Exception as e:
			print(e)

if __name__ == '__main__':
	get_proxies = GetProxy()
	get_proxies.run()