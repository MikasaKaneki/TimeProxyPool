from fake_useragent import UserAgent, FakeUserAgent, FakeUserAgentError
import random
import requests
import json
from ProxyPool.DataBase import DataBase


def GetHtmlContent(url, options={}):
    try:
        useragent = UserAgent()
    except FakeUserAgentError:
        pass
    headers = {
        "User-Agent": useragent.random,
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8'
    }

    headers = dict(headers, **options)
    print('Getting', url)
    try:
        respones = requests.get(url, headers=headers)
        print("GET  RESULT", url, respones.status_code)
        if (respones.status_code == 200):
            return respones.text
    except:
        print("GET  ERROR", url, respones.status_code)
        return None


def Get_ip181():
    db = DataBase()
    url = "http://www.ip181.com/"
    html = GetHtmlContent(url)
    dictIP = json.loads(html)
    for item in dictIP['RESULT']:
        db.AddItem(item['ip'], item['port'])
    return None
