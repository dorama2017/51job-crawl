import logging
#!/usr/bin/env python
# coding=utf-8
import requests
from bs4 import BeautifulSoup
LOG_LEVEL = logging.INFO    # 日志等级
POOL_MAXSIZE = 8  # 线程池最大容量
from selenium import webdriver

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
with open('cookie.txt',"r") as f:    #设置文件对象
    cookie = f.read()
HEADERS = {
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36"
    "(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
    "Cookie": cookie
}

senioraccountant="https://search.51job.com/list/030200%252c040000%252c020000%252c010000,000000,0401%252c0402%252c0444%252c0403%252c0404,00,9,99,+,2,{}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
liantong="https://search.51job.com/list/030200%252c040000%252c020000%252c010000,000000,0400,39%252c31,9,99,%25E8%2581%2594%25E9%2580%259A,1,{}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
dianxin="https://search.51job.com/list/030200%252c040000%252c020000%252c010000,000000,0400,39%252c31,9,99,%25E7%2594%25B5%25E4%25BF%25A1,1,{}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="

yidong="https://search.51job.com/list/030200%252c040000%252c020000%252c010000,000000,0400,39%252c31,9,99,%25E7%25A7%25BB%25E5%258A%25A8,1,{}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
combine ="https://search.51job.com/list/010000%252c030200%252c040000%252c020000,000000,0400%252c3300%252c8300,00,9,99,+,2,{}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
# "https://search.51job.com/list/040000,000000,0000,00,9,99,%25E8%25B4%25A2%25E5%258A%25A1%2520%25E6%25B7%25B1%25E5%259C%25B3,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
guangzhou ="https://search.51job.com/list/000000,000000,0000,00,9,99,%25E8%25B4%25A2%25E5%258A%25A1%2520%25E5%25B9%25BF%25E5%25B7%259E,2,{}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
shanghai = "https://search.51job.com/list/000000,000000,0000,00,9,99,%25E4%25B8%258A%25E6%25B5%25B7%2B%25E8%25B4%25A2%25E5%258A%25A1,2,{}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
#bejing=
beijing = "https://search.51job.com/list/010000,000000,0000,00,9,99,%25E8%25B4%25A2%25E5%258A%25A1,2,{}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
START_URL = (
    senioraccountant
)

urls = [START_URL.format(p) for p in range(1, 400)]

for url in urls[334:]:
    N=urls.index(url) + 1

    logger.info("爬取第 {} 页".format(urls.index(url) + 1))
    html = requests.get(url, headers=HEADERS)
    driver = webdriver.Chrome()



    driver.get(url)
    driver.add_cookie(cookie_dict={"value": cookie, "name": "51job"})
    driver.implicitly_wait(20)
    #html = requests.get(url, headers=HEADERS).content.decode("gbk")
    content = driver.page_source.encode('utf-8')
    content2=  content.decode('utf-8')
    #print(content2)
    file_handle=open("senioraccountant\\"+str(N)+'.txt',mode='w',encoding='utf-8')
    file_handle.write(content2)
    file_handle.close()




