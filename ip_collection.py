# -*- coding:utf-8 -*-
# 这里负责代理IP的采集工作
from proxy_redis import ProxyRedis
from multiprocessing import Process
from concurrent.futures import ThreadPoolExecutor
import requests
from lxml import etree
import time

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}


def get_kuai_ip(red):
    for i in range(1, 100):
        url = f'https://free.kuaidaili.com/free/intr/{i}/'
        resp = requests.get(url=url, headers=headers)
        tree = etree.HTML(resp.text)
        trs = tree.xpath('//table//tr')
        for tr in trs:
            ip = tr.xpath('./td[1]/text()')  # IP
            port = tr.xpath('./td[2]/text()')  # PORT
            if not ip:
                continue
            ip = ip[0]
            port = port[0]
            proxy_ip = ip + ':' + port
            # print(proxy_ip)
            red.add_proxy_ip(proxy_ip)  # 增加新的ip地址
        time.sleep(20)


def get_buzhidao_ip(red):
    url = 'https://ip.jiangxianli.com/?page=1'
    resp = requests.get(url=url, headers=headers)
    tree = etree.HTML(resp.text)
    trs = tree.xpath('//table//tr')
    for tr in trs:
        ip = tr.xpath('./td[1]/text()')
        port = tr.xpath('./td[2]/text()')
        if not ip:
            continue
        ip = ip[0]
        port = port[0]
        proxy_ip = ip + ':' + port
        # print(proxy_ip)
        red.add_proxy_ip(proxy_ip)  # 增加新的ip地址


def run():  # 启动爬虫
    red = ProxyRedis()  # 创建好red存储
    t = ThreadPoolExecutor(2)
    while True:
        try:
            t.submit(get_kuai_ip, red)  # 采集快代理
            t.submit(get_buzhidao_ip, red)  # 采集不知名的代理
        except Exception as e:
            print('出现错误 >> ', e)
            continue
        time.sleep(60)  # 每分钟跑一次

if __name__ == '__main__':
    run()
