# -*- coding: UTF-8 -*-
'''适用于http://www.yaoqi.la/'''
import requests
from bs4 import BeautifulSoup
import os
headers={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
#浏览器请求头
start_url=input("请输入该漫画的首页地址：")
P_url=start_url.rsplit('/',1)[0]+'/'
#地址前缀
start_html = requests.get(start_url, headers=headers)
start_html.encoding = start_html.apparent_encoding
Soup = BeautifulSoup(start_html.text,'lxml')
title=Soup.h1.get_text()
path=title
os.makedirs(os.path.join("/home/virgil/图片/adult_only",path))
os.chdir("/home/virgil/图片/adult_only/"+path)

def get_sexy(start_url):
    global headers
    global P_url
    try:
        start_html = requests.get(start_url, headers=headers)
        Soup = BeautifulSoup(start_html.text, 'lxml')
        img_url = Soup.find('li', class_='left').find('img')['src']
        name=img_url[-7:-4]
        name=name.split('i')
        name = name[-1]
        img = requests.get(img_url, headers=headers)
        print(name)
        f=open(name+'.jpg','ab')
        f.write(img.content)
        f.close()
        next_url = P_url + Soup.find('div', class_='dede_pages').find_all('li')[-1].find('a')['href']
        return get_sexy(next_url)
    except:
        print("好东西我都给你存起来了，兄弟！")
get_sexy(start_url)





