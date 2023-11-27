import pymongo
import pandas as pd
import jieba
import re
# 设置MongoDB连接信息
client = pymongo.MongoClient('localhost',27017)
cn_78 = client['51job']
project_info =cn_78['senioraccountant_href']
data = pd.DataFrame(list(project_info.find()))
print(data)

#pattern = re.compile("[^\u4e00-\u9fa5^a-z^A-Z^0-9]")    #只保留中英文、数字，去掉符号
#data['string']=data['要求'].apply(lambda x: re.sub(pattern,'',x.replace(' ','')))
#data['fenci']=data['string'].apply(lambda x: jieba.lcut(x))
separator=  r'[\<./s+//a-z/*?>]'
data['separa']=data['要求'].apply(lambda x: re.split(separator,x))


data ['separa2']=data['要求'].apply(lambda x: re.sub(separator,"",x.replace(' ','')))
print(data['separa2'])
data.to_excel('test.xlsx',encoding="utf-8")