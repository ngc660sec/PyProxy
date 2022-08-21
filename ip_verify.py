# -*- coding:utf-8 -*-
# 负责IP代理的验证工作
import time

from proxy_redis import ProxyRedis
import asyncio
import aiohttp


async def verify_one(ip, sem, red):
    timeout = aiohttp.ClientTimeout(total=10)  # 10s 没回来就报错
    async with sem:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("http://www.baidu.com", proxy="http://" + ip, timeout=timeout) as resp:
                    page_source = await resp.text()
                    if resp.status in [200, 302]:
                        print('[*]此IP可用 >> ', ip)
                        red.set_max_score(ip)
                    else:
                        # 有问题，扣分
                        print('[-]此IP不可用 >> ', ip)
                        red.des_incrby(ip)
        
        except Exception as e:
            print('[-]此IP不可用 >> ', ip)
            red.desc_incrby(ip)


async def main(red):
    # 1.把ip全部查出来
    all_proxies = red.get_all_proxy()
    sem = asyncio.Semaphore(30)
    tasks = []
    for ip in all_proxies:
        tasks.append(asyncio.create_task(verify_one(ip, sem, red)))
    await asyncio.wait(tasks)


def run():
    red = ProxyRedis()
    time.sleep(10)
    while True:
        try:
            asyncio.run(main(red))
            time.sleep(100)
        except Exception as e:
            print('出现错误 >> ', e)
            time.sleep(100)


if __name__ == '__main__':
    run()
