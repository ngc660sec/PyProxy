# -*- coding:utf-8 -*-
import redis
import random
from settings import *


class ProxyRedis:
    # self.red 链接
    def __init__(self):
        self.red = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            db=REDIS_DB,
            password=REDIS_PASSWORD,
            decode_responses=True,
        )
    
    """
    1. 存储数据
    2. 校验所有的IP，查询所有的IP
    3. 分值拉满 当IP可用时
    4. 扣分 ip 不可用
    5. 查询可用代理IP
        先给满分的
        没有满分的，给有分的
        如果都是没有分，不给
    """
    
    def add_proxy_ip(self, ip):
        #  1.判断是否有IP
        if not self.red.zscore(REDIS_KEY, ip):
            self.red.zadd(REDIS_KEY, {ip: DEFAULT_SCORE})
            print('[*]采集新的IP >> ', ip)
        else:
            print('[-]采集重复IP >> ', ip)
    
    def get_all_proxy(self):
        return self.red.zrange(REDIS_KEY, 0, -1)
    
    def set_max_score(self, ip):
        self.red.zadd(REDIS_KEY, {ip: '100'})
    
    def desc_incrby(self, ip):
        #  先查询出分值
        score = self.red.zscore(REDIS_KEY, ip)
        #  如果分值已经没了 可以删除
        if score and score > 0:
            self.red.zincrby(REDIS_KEY, -1, ip)  # 增加分数的函数,增加-1分
        #  如果分值还有，就扣一分
        else:
            self.red.zrem(REDIS_KEY, ip)  # # 删除ip
    
    def get_keyong_proxy(self):
        ips = self.red.zrangebyscore(REDIS_KEY, MAX_SCORE, MAX_SCORE, 0, -1)  # 最小分100，最大100，从0取到-1
        if ips:
            return random.choice(ips)  # 随机抽取一个返回
        else:  # 没有满分的
            ips = self.red.zrangebyscore(REDIS_KEY, DEFAULT_SCORE + 1, 99, 0, -1)
            #  判断
            if ips:
                return random.choice(ips)
            else:
                print('没有IP了')
                return None
