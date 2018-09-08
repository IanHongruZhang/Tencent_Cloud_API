import hmac
import hashlib
import base64
import time
import random

class decode:
    def __init__(self):
        self.keyset = []
        with open("APPID.txt","rb") as f1:
            with open("SECRETID.txt","rb") as f2:
                with open("SECRETKEY.txt","rb") as f3:
                    for (appid,secretid,secretkey) in zip(f1,f2,f3):
                        list_set = list(map(lambda x:bytes.decode(x).strip("\r\n"),list((appid, secretid, secretkey))))
                        self.keyset.append(list_set)

    #keyset = [[appid,secret_id,secret_key],...] keyset为一个绑定三个ID的二维数组
    #keyset_length =  8 # 现在有8个数组

    def get_parameters(self,keyset,i):
        appid = keyset[i][0]
        bucket = "tencentyun"
        secret_id = keyset[i][1]
        secret_key = keyset[i][2]
        expired = int(time.time()) + 2592000
        onceExpired = 0
        current = str(int(time.time()))
        rdm = ''.join(random.choice("0123456789") for i in range(10))
        userid = "0"
        fileid = "tencentyunSignTest"
        srcStr = 'a='+appid+'&b='+ bucket + '&k=' + secret_id + '&e=' + str(expired) + '&t=' + current + '&r=' + rdm + '&f='
        return srcStr,appid,secret_key

    def encrypt(self,srcStr,appid,secret_key):
        signature = bytes(srcStr,encoding='utf-8')
        secretkey = bytes(secret_key,encoding='utf-8')
        my_sign = hmac.new(secretkey,signature,digestmod=hashlib.sha1).digest()
        sign = base64.b64encode(my_sign + signature)
        str_sign = bytes.decode(sign)
        return str_sign

    def execute(self,index):
        keyset = self.keyset
        srcStr, appid, secret_key = self.get_parameters(keyset,index)
        str_sign = self.encrypt(srcStr,appid,secret_key)
        return str_sign,appid

