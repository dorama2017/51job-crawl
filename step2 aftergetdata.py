import re
import ast
import logging
LOG_LEVEL = logging.INFO



from pymongo import MongoClient
client =  MongoClient('localhost', 27017)
client = MongoClient()# 连接的数据库
collection = client['51job']# 连接的表
col = collection['senioraccountant']


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
for i in range(1,208):

    logger.info("添加第 {} 个文件".format(i))
    f = open("senioraccountant\\"+str(i)+'.txt',"r",encoding='utf-8')   #设置文件对象
    A1 = f.read()     #将txt文件的所有内容读入到字符串str中
    #print(str)
    f.close()   #将文件关闭
    try:
        #  a = re.findall(r'\"engine_jds\":\[(.+?)\],\"jobid_count\"',A1)  #只有一页的
        a = re.findall(r'\"top_ads\":.],\"auction_ads\":..,\"market_ads\":.],\"engine_jds\":(.+?),\"jobid_count\"', A1)    #很多页的

       # print(a[0])

        list = ast.literal_eval(a[0])
     #   print(list)
        for item in list:
            col.insert_one(item)
    except Exception as e:
        logger.info("第 {} 个文件添加失败".format(i))
        pass
    continue