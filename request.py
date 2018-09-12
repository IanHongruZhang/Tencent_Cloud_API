#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

from encrypt import Decode
#from filter import cleaning
import requests
import time
import random
import json
import urllib
import re
from bs4 import BeautifulSoup
import pprint
try:
    import cPickle as pickle
except:
    import pickle

class Get:
    """


    """
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
        response_info = html.content
        return response_info


class Parse:
    """


    """
    def __init__(self,html_text):
        self.html_text = html_text

    def parse_to_json(self):
        try:
            json_file = json.dump(self.html_text)
            for item in json_file["data"]["items"]:
                item_string = item["itemstring"]
                return item_string
        except Exception as e:
            item_string = None
        return item_string

    def parse_to_bs4(self):
        try:
            html_soup = BeautifulSoup(self.html_text,'lxml')
            html_soup_p = html_soup.find("p").get_text()
            text = html_soup_p.decode("utf-8")
            pattern = re.compile('string":"\[.*?]')
            words = re.findall(pattern, text)
        except Exception as e:
            words = None;
        return words


class Save_load:
    """


    """
    def __init__(self,list_json,file_name):
        self.json = list_json
        self.file_name = file_name

    def save(self):
        with open(self.file_name,"wb") as pickle_files:
            pickle.dump(self.list_json,pickle_files)

    def load(self):
        with open(self.file_name,"rb") as pickel_files:
            list_new_json = pickle.load(pickel_files)
            return list_new_json

if __name__ == "__main__":
    def exec_encrypt(index):
        cl = Decode()
        str_sign,appid = cl.execute(index)
        return str_sign,appid

    def exec_get(url,appid,str_sign,image_name):
        cl = Get(url,appid,str_sign,image_name)
        responseinfo = cl.post()
        return responseinfo

    def exec_parse(html_text):
        cl = Parse(html_text)
        item_string = cl.parse_to_json()
        return item_string

    def exec_save():
        cl = Save_load()
        cl.save()







