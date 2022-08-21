# -*- coding:utf-8 -*-
from ip_api import run as api_run
from ip_collection import run as coll_run
from ip_verify import run as veri_run

from multiprocessing import Process
def run():
    # 启动三个进程
    p1 = Process(target=api_run)
    p2 = Process(target=coll_run)
    p3 = Process(target=veri_run)
    
    p1.start()
    p2.start()
    p3.start()
    
    
if __name__ == '__main__':
    run()
