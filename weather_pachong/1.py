#多进程爬取天气
import requests
import re
import os
import prettytable as pt
from threading import Thread
import time

datas=['02月18日', '02月19日', '02月20日', '02月21日', '02月22日', '02月23日', '02月24日']
s1=re.compile(r">(\d\d月\d\d日)")	#日期
s2=re.compile(r'temp">([\u4e00-\u9fa5]+){1,5}')		#天气
s3=re.compile(r'<dd class="txt">(.+)℃ ~ <b>(-?\d+)</b>℃</dd>')	#温度
s4=re.compile(r'">(\w+)</b></dd>')	#空气质量
#s4_1=re.compile(r'title="空气质量：(.+)">(.+)</b>')		  
s5=re.compile(r'<dd class="txt">(\w+)\s(\w+)</dd>')	#风力
	
def getweather(data):
	url="http://www.tianqi.com/zhouzhi/7/"
	txt=requests.get(url,headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36","Host": "www.tianqi.com"}).text
	# test1=s1.findall(txt)
	# test2=s2.findall(txt)	
	# test3=s3.findall(txt)
	# test4=s4.findall(txt)
	# test5=s5.findall(txt)
	riqi=s1.search(txt).group(1)
	print(riqi)
	
start=time.time()
for data in datas:
	p=Thread(target=getweather,args=(data,))
	p.start()
	p.join()
end=time.time()
print("共花费%f秒"%(end-start))














	
# table1=pt.PrettyTable(["日期","天气","温度","空气质量","风向"])
# for i in range(7):
	# table1.add_row([test1[i],test2[i],test3[i],test4[i],test5[i]])
# print(table1)
	
	
	
	
	
		
