# coding=UTF-8

import requests

def getUrl(url):
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    }
    #url = "http://beautycareapp.com/" # 等价下面的
    response = requests.get(url, headers=headers).text
    print(response)
    return response
