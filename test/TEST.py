import base64
import json

import requests
from Crypto.Cipher import AES


class EncryptDate:
    def __init__(self, key):
        self.key = key.encode("utf-8")  # 初始化密钥
        self.length = AES.block_size  # 初始化数据块大小
        self.aes = AES.new(self.key, AES.MODE_ECB)  # 初始化AES,ECB模式的实例
        # 截断函数，去除填充的字符
        self.unpad = lambda date: date[0:-ord(date[-1])]

    def pad(self, text):
        """
        #填充函数，使被加密数据的字节码长度是block_size的整数倍
        """
        count = len(text.encode('utf-8'))
        add = self.length - (count % self.length)
        entext = text + (chr(add) * add)
        return entext

    def encrypt(self, encrData):  # 加密函数
        res = self.aes.encrypt(self.pad(encrData).encode("utf8"))
        msg = str(base64.b64encode(res), encoding="utf8")
        return msg

    def decrypt(self, decrData):  # 解密函数
        res = base64.decodebytes(decrData.encode("utf8"))
        msg = self.aes.decrypt(res).decode("utf8")
        return self.unpad(msg)


eg = EncryptDate("b7de913d2ecbab01fb15a84db1f501c0")  # 这里密钥的长度必须是16的倍数
data = '{"APP_Code":"PC_BASE002","ShowSYS":false,"tablename":"BASE002M","tableHead":[{"label":"工厂代号","prop":"factory_code","enumData":[],"width":110,"FieldDisplay":true,"Sort":0},{"label":"工厂名称","prop":"factory_name","enumData":[],"width":200,"FieldDisplay":true,"Sort":0},{"label":"邮编","prop":"zip_code","enumData":[],"width":100,"FieldDisplay":true,"Sort":0},{"label":"地址","prop":"address","enumData":[],"width":257,"FieldDisplay":true,"Sort":0},{"label":"备注","prop":"note","enumData":[],"width":200,"FieldDisplay":true,"Sort":0}]}'
res = eg.encrypt(str(data))
print(res)
print(eg.decrypt(res))

































# import base64
# from Crypto.Cipher import AES
#
# '''
# 采用AES对称加密算法
# '''
# # str不是32的倍数那就补足为16的倍数
# def add_to_32(value):
#     while len(value) % 32 != 0:
#         value += '\0'
#     return str.encode(value)  # 返回bytes
#
# def add_to_16(value):
#     while len(value) % 16 != 0:
#         value += '\0'
#     return str.encode(value)  # 返回bytes
#
# #加密方法
# def encrypt_oracle(text):
#     # 秘钥
#     key = '12121c3b08deb2203311a743b9693fd6'
#     # 待加密文本
#     # 初始化加密器
#     aes = AES.new(add_to_32(key), AES.MODE_ECB)
#     #先进行aes加密
#     encrypt_aes = aes.encrypt(add_to_16(text))
#     #用base64转成字符串形式
#     encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')  # 执行加密并转码返回bytes
#     print(encrypted_text)
#     return encrypted_text
# #解密方法
# def decrypt_oralce(text):
#     # 秘钥
#     key = 'VW1lMjAxMlRyaXAwMzA5AA=='
#     # 密文
#     # 初始化加密器
#     aes = AES.new(add_to_16(key), AES.MODE_ECB)
#     #优先逆向解密base64成bytes
#     base64_decrypted = base64.decodebytes(text.encode(encoding='utf-8'))
#     #执行解密密并转码返回str
#     decrypted_text = str(aes.decrypt(base64_decrypted),encoding='utf-8').replace('\0','')
#     print('decrypted_text',decrypted_text)
#     return decrypted_text
#
# if __name__ == '__main__':
#
#     text = '{"APP_Code":"PC_CRM002","ShowSYS":false,"tablename":"CRM002M","tableHead":[{"label":"客户代号","prop":"customer_code","enumData":[],"width":120,"FieldDisplay":true,"Sort":0},{"label":"客户名称","prop":"customer_name","enumData":[],"width":200,"FieldDisplay":true,"Sort":0},{"label":"联系人","prop":"customer_staff","enumData":[],"width":74,"FieldDisplay":true,"Sort":0},{"label":"职位","prop":"staff_job","enumData":[],"width":80,"FieldDisplay":true,"Sort":0},{"label":"电话","prop":"customer_phone","enumData":[],"width":110,"FieldDisplay":true,"Sort":0},{"label":"邮箱","prop":"zip_code","enumData":[],"width":120,"FieldDisplay":true,"Sort":0},{"label":"地址","prop":"customer_address","enumData":[],"width":400,"FieldDisplay":true,"Sort":0},{"label":"备注","prop":"note","enumData":[],"width":400,"FieldDisplay":true,"Sort":0}]}'
#     entrypted_text = encrypt_oracle(text)
#
#     decrypt_oralce(entrypted_text)
# key='12121c3b08deb2203311a743b9693fd6'
# data='{"APP_Code":"PC_CRM002","ShowSYS":false,"tablename":"CRM002M","tableHead":[{"label":"客户代号","prop":"customer_code","enumData":[],"width":120,"FieldDisplay":true,"Sort":0},{"label":"客户名称","prop":"customer_name","enumData":[],"width":200,"FieldDisplay":true,"Sort":0},{"label":"联系人","prop":"customer_staff","enumData":[],"width":74,"FieldDisplay":true,"Sort":0},{"label":"职位","prop":"staff_job","enumData":[],"width":80,"FieldDisplay":true,"Sort":0},{"label":"电话","prop":"customer_phone","enumData":[],"width":110,"FieldDisplay":true,"Sort":0},{"label":"邮箱","prop":"zip_code","enumData":[],"width":120,"FieldDisplay":true,"Sort":0},{"label":"地址","prop":"customer_address","enumData":[],"width":400,"FieldDisplay":true,"Sort":0},{"label":"备注","prop":"note","enumData":[],"width":400,"FieldDisplay":true,"Sort":0}]}'
# encrypt(key,data)