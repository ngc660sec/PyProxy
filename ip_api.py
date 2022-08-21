# -*- coding:utf-8 -*-
# 负责提供代理IP的接口
from proxy_redis import ProxyRedis
from sanic import Sanic, json
from sanic_cors import CORS
from settings import *

# 提供给外界一个http接口，外界通过访问接口来获取IP
red = ProxyRedis()

# 1.创建app
app = Sanic('IP')  # 随便给个名字就可以

# 2.解决跨域问题
CORS(app)


# 3.能够处理HTTP请求的函数
@app.route('/')  # 当访问这个页面的时候,自动执行这个函数
def clhttp(req):
    ip = red.get_keyong_proxy()
    return json({'ip': ip})


def run():
    app.run(host=API_ADDRESS, port=API_PORT)


if __name__ == '__main__':
    run()
