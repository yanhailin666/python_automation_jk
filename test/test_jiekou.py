import requests
from test_code.TEST import *

url='http://emes.gdshangji.com:8000/api/commoncall'

headers={
"Host": "emes.gdshangji.com:8000",
"Proxy-Connection": "keep-alive",
"Content-Length": "970",
"Accept": "application/json, text/plain, */*",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
"Content-Type": "application/json;charset=UTF-8",
"Origin": "http://emes.gdshangji.com",
"Referer": "http://emes.gdshangji.com/",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,zh;q=0.9",
}
eg = EncryptDate("b7de913d2ecbab01fb15a84db1f501c0")
data = '{"APP_Code":"PC_BASE002","ShowSYS":false,"tablename":"BASE002M","tableHead":[{"label":"工厂代号","prop":"factory_code","enumData":[],"width":110,"FieldDisplay":true,"Sort":0},{"label":"工厂名称","prop":"factory_name","enumData":[],"width":200,"FieldDisplay":true,"Sort":0},{"label":"邮编","prop":"zip_code","enumData":[],"width":100,"FieldDisplay":true,"Sort":0},{"label":"地址","prop":"address","enumData":[],"width":257,"FieldDisplay":true,"Sort":0},{"label":"备注","prop":"note","enumData":[],"width":200,"FieldDisplay":true,"Sort":0}]}'
data4=eg.encrypt(str(data))
#data='{"IP4":"","IsRasRequst":false,"IsRasResult":false,"MAC":"","RasResultKey":"","UserToken":"74c8fa24-266e-411d-b5ca-e307a798e08d","DllName":"SJ_SYSAPI","ClassName":"SJ_SYSAPI.SYS","Method":"SaveModuleConfigPanelH","Data":"Jix06XN6AhMC2Wpze48o8Ge2MppJDdMin0F5HHV4Fv1JXsHuPlvf248asEW/xGAA594e3+7U9HR/AcpZzx95g3EOREP8cIK1bkeLLMY7OcTEbDPYA+m2E8u+xtiVxeqkp7FTlUxYfUrsIYMq9WZlpfMhwg2ZWazVRxxGxNFhaHWix4joK/0kGosx535LOM8iJc1+Xppj9Tt7YIqMQmTQxVRyBAXlvb3zooqvD78iE93EeGTR1+Id04CoTIFjlyHafpgT6WPzuoqvcMBtZu81ei2gGSaZK/GQickw15KeOp8Z2L+nJUfbhEWehYN2T5O7ctvASqp8538/p+LSuibXnoxjX0AO72DihM5TDqzWSy3/ZjOHRnwYSpMOS8P1fYyBzoKGV1bMLgrIuaNjFi2VbnmVDXP30xQEd/Y8SCMGKkopocNsCnw3TN1k+tdXBlBhGRJOh/l5rM16uvDctsXGmdchfb3QxxY6bBtpEsEujLsrlm332peQo9+TTTu8HKtdJk9Tgycn6BhZf4ux1V4NXOs0ma1Xjb4ixKH0qDwk34Fr7+t1uRshwGK2RX6H/a4utPWK6TwKtgbGkBcnyrtKhY5kbGkZxeI7443EsN796I1eMQ/iaHckJRzMQi+5x+533o8MT85EH+oVrvDjPMKvK+o5mgWI0Y+1abGyDMpKaceWOtKvG/eVxBPjbKtq2Mm60yfnRdmcQEv4ov8yKVtdbOkJtoNNRrHCZyv7wp4yr4c="}'
data1='{"IP4":"","IsRasRequst":false,"IsRasResult":false,"MAC":"","RasResultKey":"","UserToken":"74c8fa24-266e-411d-b5ca-e307a798e08d","DllName":"SJ_SYSAPI","ClassName":"SJ_SYSAPI.SYS","Method":"SaveModuleConfigPanelH","Data":"'
data3='"}'
data2=data1+data4+data3#请求参数拼接
print(data2)
aa=requests.request("POST",url=url,data=data2,headers=headers)#请求
print(aa.text)
print((aa.cookies))
print(aa)