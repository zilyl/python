# coding: utf-8
#author:bdb0y

import requests
import re
from bs4 import BeautifulSoup

file = open("/usr/share/url.txt")
lines=file.readlines()

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

print("URL\t\t\t\t\t备案信息")
for i in lines:
    #i=i.strip("\n")
    #print(i)
    try:
        url="https://www.aizhan.com/seo/"+i.strip()
        #print(url)
        r=requests.get(url,headers=header)
        response=r.text
              
        #正则表达式处理匹配到的数据
        flag1=re.search('<span id="icp_company">[\u4E00-\u9FA5]+</span></li>',response)
        a=flag1.group()
        #print(a)
        
        data=re.search('[\u4E00-\u9FA5]+',a)
        b=data.group()
        
        #输出格式
        if b:
            print('%-20s'%i.strip()+"\t\t\t"+b)
        else:
            print("未查到相关信息")      
        
    except:
        pass
    
