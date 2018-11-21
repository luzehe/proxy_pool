from redis import StrictRedis

# 创建redis数据库客户端
redis_clien = StrictRedis

# Flask Host地址
FLASK_HOST = '127.0.0.1'

# Flask Port地址
FLASK_PORT = '7890'

# 要求的可用proxy数量
PROXY_REQUIRDE_NUMBER = 100

# proxy更新时间
PROXY_UPDATE_TIME = 60*5
