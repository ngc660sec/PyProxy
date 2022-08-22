# -*- coding:utf-8 -*-
# 代理池配置文件

# Redis地址
REDIS_HOST = '127.0.0.1'

# Rdeis端口
REDIS_PORT = 6379

# Redis数据库
REDIS_DB = 4

# Rdeis数据库密码
REDIS_PASSWORD = "admin"

# 存储在redis中的代理ip的key， 建议不更换
REDIS_KEY = "proxy_ip"

# api接口IP
API_ADDRESS = '127.0.0.1'

# api接口端口
API_PORT = 10010

# 设置快代理的爬取页数
KUAI_PAGE = 100

# 默认IP分值
DEFAULT_SCORE = 10

# 满分
MAX_SCORE = 100


