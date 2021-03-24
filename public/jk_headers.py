def url():
   url='http://emes.gdshangji.com:8000/api/commoncall'
   return url

def headers():
    headers = {
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
    return headers