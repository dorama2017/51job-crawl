import pymongo
import pandas as pd
import logging
#!/usr/bin/env python
# coding=utf-8
import requests
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup
LOG_LEVEL = logging.INFO    # 日志等级
POOL_MAXSIZE = 8  # 线程池最大容量
from selenium import webdriver
import random
from selenium.webdriver.common.by import By
def get_logger():
    """
    创建日志实例
    """
    formatter = logging.Formatter("%(asctime)s - %(message)s")
    logger = logging.getLogger("monitor")
    logger.setLevel(LOG_LEVEL)

    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger
logger = get_logger()
# 设置MongoDB连接信息
client = pymongo.MongoClient('localhost',27017)
cn_78 = client['51job']
project_info =cn_78['senioraccountant']
job_hrefs = pd.DataFrame(list(project_info.find()))[['job_href']].values.tolist()
# 删除mongodb中的_id字段del data['_id']#

with open('cookie.txt',"r") as f:    #设置文件对象
    cookie = f.read()
ip_list=[                       #ip存放地址
    '10.210.35.209:8080', '10.210.35.214:8080', '10.210.35.219:8080', '10.210.35.200:8080', '10.210.35.168:8080',
    '10.210.35.138:8080', '10.210.35.170:8080', '10.210.35.183:8080', '10.210.35.149:8080', '10.210.35.232:8080',
    '10.210.209.199:8080', '10.210.35.157:8080', '10.210.35.182:8080', '10.210.35.210:8080', '10.210.35.240:8080',
    '10.210.35.172:8080', '10.118.35.126:8080', '10.210.35.178:8080'
    ]
ip=random.choice(ip_list)
proxy_ip = 'http://' + ip
proxy_ips = 'https://' + ip
proxy = {'https': proxy_ips, 'http': proxy_ip}

HEADERS = {
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36",
    "Cookie": cookie
}

for job_href in job_hrefs[339:]:
    N = job_hrefs.index(job_href) + 1
    url = job_href[0].replace("\\","")


    logger.info("爬取第 {} 页".format(N))
  #  html = requests.get(url, headers=HEADERS, proxies=proxy)
    html = requests.get(url, headers=HEADERS)
    driver = webdriver.Chrome()



    driver.get(url)
    driver.add_cookie(cookie_dict={"value": cookie, "name": "51job"})
    #driver.wait(2000)
    driver.implicitly_wait(2000)
    try:


        #html = requests.get(url, headers=HEADERS).content.decode("gbk")
        content = driver.page_source.encode('utf-8')
        content2=  content.decode('utf-8')
        #print(content2)
        file_handle=open("senioraccountant_job_href\\"+str(N)+'.txt',mode='w',encoding='utf-8')
        file_handle.write('url:'+url+'\n'+content2)
        file_handle.close()

        #滑块定位失败，能挪动也没用
    except Exception as e:
        button= driver.find_elements(By.CLASS_NAME, 'nc_iconfont btn_slide')
        print("定位滑块")
        ActionChains(driver).move_by_offset(258,0).click_and_hold().perform()



