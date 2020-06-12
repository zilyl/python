#小说爬虫
import requests
import re
url="http://www.xbiquge.la/29/29948/"
txt=requests.get(url,headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36","Host":"www.xbiquge.la"}).content.decode("utf-8")
#print(txt)
m1=re.compile(r"<dd><a href='(.+)' >(.+)</a>")
bt=m1.findall(txt)
print("目录加载完成")

for i in bt:
	try:
		url2="http://www.xbiquge.la/%s"%(i[0])
		zw1=requests.get(url2).content.decode("utf-8")
	except UnicodeEncodeError:
		continue
	m2=re.compile(r'<div id="content">(.+)<p>')
	zw2=m2.findall(zw1)
	print("开始下载----------",i[1])
	for k in range(len(zw2)):
		zw2[k]=re.sub("<br />","",zw2[k])
		zw2[k]=re.sub("&nbsp;&nbsp;&nbsp;&nbsp;","",zw2[k])
		with open("万界之最强孙悟空.txt","a+",encoding="utf-8") as f:
			f.write("\n%s\n"%i[1])
			f.write(zw2[k])
