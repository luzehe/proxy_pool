## 爬虫ip代理池



#### 作者和版本号

author：`Lu Zehe`

version：`proxy_pool 1.0`



#### 测试环境

- 操作系统：`Windows10`
- python版本：`python3.71`
- redis版本：`redis-cli 3.2.100`



#### 需要用到的pythion库

- `requests`
- `lxml`
- `flask`
- `gevent`
- `retrying`
- `redis`



#### 下载安装本项目

- 下载`[ProxyPool-1.0.tar.gz](https://github.com/luzehe/proxy_pool/blob/master/proxy_pool/ProxyPool-1.0.tar.gz)`
- 解压`ProxyPool-1.0.tar.gz`到本地
- 找到setup.py文件，并在此路径下执行命令：`python setup.py install`



#### 使用方法

- 方法一：
  - （1）执行main.py和FlaskApi.py程序
  - （2）用浏览器打开`http://127.0.0.1：7890/http`获取HTTP类型的proxy，`http://127.0.0.1：7890`/https获取HTTPS类型的proxy。
  - （3）当你开启前面两个程序时，你可以在自己的爬虫项目中，通过`proxy = requests.get("http://127.0.0.1：7890/http").text`方法来获取代理IP。
- 方法二：
  - `import getProxyFromRedis`模块，通过创建`obj = getProxyFromRedis.GetOneProxy()` 对象，调用`obj.getOneProxy(proxy_type='http')方法，返回一个可用ip。`



#### 注意

- 此项目默认对已经抓取过的代理ip进行指纹去重，如过不想去重可以在`getFreeProxy`中修改`save.item`方法。
- 代理IP默认保存在redis数据库中，key为"http"，https"，"http_fingerprint"，"https_fingerprint"，其中fingerprin为代理IP的指纹，目的是进行ip去重。
- 可在`getFreeProxy`模块中加入自己的proxy抓取代码。



#### 问题反馈

- 本项目将持续更新，如果有任何bug或者问题，可以联系微信：luzehe



#### 



#### 
