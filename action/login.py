import requests
from public.jk_headers import *

url = url()
headers = headers()
def login(data):
    fh_data=requests.request("POST",url=url,data=data,headers=headers, allow_redirects=False)
    if fh_data.status_code==200:
        print("登录成功")
        fh_UserToken=fh_data.json()
        aa=fh_UserToken['RetData']
        print(aa)
    else:
        print("登录失败")



data='{"DllName":"SJ_SYSAPI","ClassName":"SJ_SYSAPI.User","Method":"Login","IP4":"","MAC":"MAC","IsRasRequst":false,"IsRasResult":false,"RasResultKey":"","UserToken":"","Data":{"CompanyCode":"955380","CompanyName":"佛山市顺德区赛恩特实业有限公司","UserCode":"yhl","UserPassword":"E10ADC3949BA59ABBE56E057F20F883E"}}'
data=data.encode('utf-8')
login(data)