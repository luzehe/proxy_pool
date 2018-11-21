from flask import Flask
from werkzeug.routing import BaseConverter
from redis import StrictRedis
import ProxyDecorator, setting



class RegexConverter(BaseConverter):	
	"""自定义转换器"""
	def __init__(self, url_map, *args):
		super().__init__(url_map)
		self.regex = args[0]


app = Flask(__name__)

app.url_map.converters['re'] = RegexConverter

redis_clien = setting.redis_clien()


@app.route('/<re("http|https"):proxy_type>')
def http(proxy_type):
	# 如果数据库中有proxy, 则返回proxy, 反之None
	if redis_clien.llen(proxy_type) > 0:
		proxy = redis_clien.rpop(proxy_type)
		redis_clien.lpush(proxy_type, proxy)
	else:
		proxy = None
	return proxy


if __name__ == '__main__':
	app.run(host=setting.FLASK_HOST, port=setting.FLASK_PORT, debug=True)
