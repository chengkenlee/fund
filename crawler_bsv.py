#!/usr/bin/python
# -*- coding: UTF-8 -*-

from urllib.parse import urlencode
import requests
import pymysql
from lxml import etree
from decimal import Decimal, getcontext
import sys
 
url = "https://www.feixiaohao.com/currencies/bitcoin-cash-sv/"
ua  = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"

def running():
    with requests.request('GET',url,headers = {'User-agent':ua}) as res:
        content = res.text          #获取HTML的内容
        html = etree.HTML(content)  #分析HTML，返回DOM根节点
        orders = html.xpath("//div[@class='sub']//span/text()")
        v1 = orders[3]
        print(v1)

def mmsql():
    db = pymysql.connect(host='localhost', user='root', password='rkm2018', port=3306, db='stock')
    cursor = db.cursor()
    sql = "insert into tb_eth (Codes,Sname,Vvalue,Vaddnu,Vaddpe) values('007244','安信核心混合C','%s','%s','%s');" %(a,b,c)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()

running()
