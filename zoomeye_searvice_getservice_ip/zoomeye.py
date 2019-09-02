# coding: utf-8
#zoomeye扫描器
import os
import requests
import json
 
access_token = ''
ip_list = []
 
def login():
    """
    输入用户密码 进行登录操作
    """
    global access_token
    user = input('[-] input : username :')
    passwd = input('[-] input : password :')
    data ={'username':user,'password':passwd}
    data_encoded = json.dumps(data)  # dumps 将 python 对象转换成 json 字符串
    try:
        r = requests.post('https://api.zoomeye.org/user/login',data = data_encoded)
        r_decoded = r.json() # loads() 将 json 字符串转换成 python 对象        
        access_token = r_decoded['access_token']
    except Exception as e:
        print('[-] info : username or password is wrong, please try again ')
        exit()
 
def saveStrToFile(file,str):
    """
    将字符串写入文件中
    """
    with open(file,'w') as output:
        output.write(str)
 
def saveListToFile(file,list):
    """
    将列表逐行写入文件中
    """
    s = '\n'.join(list)
    with open(file,'w') as output:
        output.write(s)
 
def apiTest():
    """
    进行 api 使用测试
    """
    with open('access_token.txt','r') as input:
        access_token = input.read()
    # 将 token 格式化并添加到 HTTP Header 中
    headers = {
        'Authorization' : 'JWT ' + access_token,
    }

    for page in range(1,11):
        try:             
            r = requests.get('https://api.zoomeye.org/host/search?query="redis"&facet=app,os&page=' + str(page),headers = headers)
            r_decoded = r.json()
            for x in r_decoded['matches']:
                print(x['ip']+":"+str(x['portinfo']['port']))
                ip_list.append(x['ip']+":"+str(x['portinfo']['port']))
            print('[-] info : count ' + str(page * 10)) 
 
        except Exception as e:
            # 若搜索请求超过 API 允许的最大条目限制 或者 全部搜索结束，则终止请求
            print('[-] info : ' + str(e))

def main():
    # 访问口令文件不存在则进行登录`操作
    if not os.path.isfile('access_token.txt'):
        print('[-] info : access_token file is not exist, please login')
        login()
        saveStrToFile('access_token.txt',access_token)
    apiTest()
    saveListToFile('ip_list.txt',ip_list)
if __name__ =='__main__':
    main()	