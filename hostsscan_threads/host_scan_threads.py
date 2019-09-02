#多线程主机扫描	作者：张豫
from sys import argv
import subprocess
import time
from threading import Thread
import os

result=[]
result1=[]
def ping1(ip):
	command="ping %s -n 1 -w 1"%(ip)	
	#result.append([ip,subprocess.call(command,stdout=open('nul','w'))])
	result.append([ip,subprocess.getoutput(command)])
	
def ping(net,start=1,end=255):
	for i in range(start,end):
		ip=net+"."+str(i)
		t=Thread(target=ping1,args=(ip,))
		t.start()

t1=time.time()

if len(argv)!=2:
	print("参数输入错误！")
	print("运行实例：")
	print("demo.py 192.168.1")
	print("语法：demo.py net")
elif len(argv)==2:
	net=argv[1]
	ping(net)
	while len(result)!=254:
		time.sleep(1)

result1=sorted(result,key=(lambda i:int(i[0].split(".")[-1])))
'''with open("result.txt","w") as f:
		f.write(str(result1))'''
for i in result1:
	zifu=str(i)
	ttl=zifu[(zifu.find("TTL=")):(zifu.find("\n",zifu.find("TTL=")))]
	ttl_str1=ttl[4:6]
	ttl_str2=ttl[4:7]
	if ttl_str1:
		if int(ttl_str1)<=64:	
			print(i[0],"\t----\tLinux","TTL=",ttl_str1)
		elif int(ttl_str2)==128:
				print(i[0],"\t----\tWindows2000","TTL=",ttl_str2)
		elif int(ttl_str2)>128:
				print(i[0],"\t----\tUnix","TTL=",ttl_str2)
		else:
			print("未知操作系统类型")
	else:
		print(i[0],"\t----\t防火墙保护中")
		
t2=time.time()
print("程序耗时%f秒"%(t2-t1))


