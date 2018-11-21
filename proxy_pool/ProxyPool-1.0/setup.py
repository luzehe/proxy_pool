from distutils.core import setup

setup(
	name='ProxyPool',
      version='1.0',
      description='redis代理池',
      author='luzehe',
      author_email='luzehe@qq.com',
      github='https://github.com/luzehe',
      WeChat='luzehe',
      py_modules=[
      	'proxy_pool.main', 
      	'proxy_pool.FlaskApi', 
      	'proxy_pool.getProxyFromRedis',
      	'proxy_pool.getFreeProxy',
      	'proxy_pool.CheckProxy',
      	'proxy_pool.getHTMLTree',
      	'proxy_pool.UAPool',
      	'proxy_pool.setting',
      	] 
    )