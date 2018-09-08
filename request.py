from encrypt import decode
import requests
import time
import random
import re
import urllib
from bs4 import BeautifulSoup

class get:
    def __init__(self,url,appid,str_sign,image_name):
        self.url = url
        self.appid = appid
        self.bucket = "tencentyun"
        self.host = 'recognition.image.myqcloud.com'
        self.headers = {
            'Host':self.host,
            'Authorization':str_sign
        }
        self.file = {
            'appid':(None,self.appid),
            'bucket':(None,self.bucket),
            'image': (image_name,open(image_name,'rb'),'image/jpeg')
        }

    def post(self):
        html = requests.post(self.url,files=self.files,headers=self.headers)
        responseinfo = html.content
        return responseinfo

class parse:
    def __init__(self,html_text):
        self.html_text = html_text

    def parse_to_json(self):
        json_dump

    def parse_to_bs4(self):
        html_soup = BeautifulSoup(self.html_text,'lxml')
        html_soup_p = html_soup.find("p").get_text()
        text = html_soup_p.decode("utf-8")
        pattern = re.compile('string":"\[.*?]')
        words = re.findall(pattern, text)
        return words

class save:


if __name__ == "__main__":
    def exec_encrypt(cl,index):
        str_sign,appid = cl.execute(index)
        return str_sign,appid

    def exec_get(cl,url,appid,str_sign,iamge_name):
        responseinfo = cl.post()
        return responseinfo

    def exec_parse():
        pass





