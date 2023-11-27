# codes
crawl employment data from 51job, including salary, location, requirements etc. 
从51job爬取薪酬、工作要求、地点等信息。

this is a relatively rough but efffective case.

代码比较粗糙，但可以用，结果见高级财务人员的薪酬和任职要求-2022年51job.xlsx

the result can be seen on 高级财务人员的薪酬和任职要求-2022年51job.xlsx

使用方法：
1、step1 爬取html
2、step2 用正则表达式将信息写入mongodb
3、step3 整理数据并写入excel
4、step4 获取工作要求，需要逐个点进岗位链接
5、step5-step6 提取工作要求中的关键词
