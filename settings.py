# -*- coding:utf-8 -*-
# 代理池配置文件

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DB = 5
REDIS_PASSWORD = "admin"
# 存储在redis中的代理ip的key， 建议不更换
REDIS_KEY = "proxy_ip"

# 默认IP分值
DEFAULT_SCORE = 10

# 满分
MAX_SCORE = 100
