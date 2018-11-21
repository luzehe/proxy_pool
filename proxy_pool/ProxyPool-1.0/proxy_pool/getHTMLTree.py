import requests, retrying
from lxml import etree
import UAPool


# @retrying.retry(stop_max_attempt_number=3)
def getHTMLTree(url, headers='', cookies=''):
	'''返回lxml.etree对象'''
	try:
		# position = url.find(':')
		# ip = requests.get('http://127.0.0.1:5000/%s' % url[:position]).text
		# proxies = {url[:position]: ip}
		if cookies and headers:
			response = requests.get(url, headers=headers, cookies=cookies, timeout=1)
		else:
			headers = {"User-Agent": UAPool.get_user_agent()}
			response = requests.get(url, headers=headers, timeout=1)
		response.encoding = response.apparent_encoding
		if response.status_code == 200:
			html = etree.HTML(response.content.decode(response.encoding))
			print('正在从"%s"中获取proxy' % response.url)
			return html
		else:
			print('状态码: %s, 该Proxy网址: %s 已失效' % (response.status_code, response.url))
			return ''
	except:
		return ''

