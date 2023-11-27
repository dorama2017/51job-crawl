import pymongo
import pandas as pd 
# 设置MongoDB连接信息
client = pymongo.MongoClient('localhost',27017)
cn_78 = client['51job']
project_info =cn_78['senioraccountant']
data = pd.DataFrame(list(project_info.find()))
# 删除mongodb中的_id字段del data['_id']#



data['degree']=data['attribute_text'].apply(lambda x: [x] if not isinstance(x, list) else x[-1])

data['wage_unit']=data['providesalary_text'].apply(lambda x: 10000 if  x[x.find("\\")-1:x.find("\\")] =="万" else 1000 if  x[x.find("\\")-1:x.find("\\")] =="千" else 0)
data['wage_date'] = data['providesalary_text'].apply(lambda x: x if not x.find("/") else x[x.find("/")+1:x.find("/")+2])
data=data[~data['wage_unit'].isin([0])]
#删除wageunit=0
data=data[~data['isIntern'].isin([1])]
#通过~取反，选取不包含数字1的行


data['min_wage']=data['providesalary_text'].apply(lambda x: x if not x.find("-") else x[:x.find("-")])
data['max_wage']=data['providesalary_text'].apply(lambda x: x if not x.find("-") else x[x.find("-")+1:x.find("\\")-1])
data['min_wage'] = pd.to_numeric(data['min_wage'])*data['wage_unit']
data['max_wage'] = pd.to_numeric(data['max_wage'])*data['wage_unit']
data['avg_wage'] = (pd.to_numeric(data['max_wage']) + pd.to_numeric(data['max_wage']))/2

#print(data[['min_wage','max_wage','wage_unit','wage_date']])
data1 = data[['job_href','job_name','company_href',
             'company_name',
             'workarea_text','companytype_text',
             'workyear','companyind_text',
             'companysize_text','degree','min_wage','max_wage','wage_date','avg_wage'
             ]]

#删除平均工资低于7k
#data1=data1[data1['avg_wage']>7000]

data1  = data1.drop_duplicates()
data1.to_excel('senioraccountant-data.xlsx',encoding="utf-8")
print(data1.head())



print(data1.info())