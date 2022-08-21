# PY代理池
Python可用的代理池

---

# 使用前须知
+ 使用前请先安装redis
+ settings.py 为默认配置文件，redis等配置信息在此文件存储
+ ip_api 为提供api默认url,如想修改，请在此文件中修改
+ runner.py 为主文件

---

# 使用方法
- 首先安装支持库
  - pip instll -r requirements.txt
- 直接启动 runner.py
  - python3 runner.py
- ![image](https://user-images.githubusercontent.com/52269948/185779097-af14949f-5d3c-4936-9f5b-95beb27bad27.png)
- 访问 `127.0.0.1:10010` 获取验证成功ip
