#!/usr/bin/python
# -*- coding: UTF-8 -*-

from urllib.parse import urlencode
import requests
import pymysql
from lxml import etree
 
url = "http://fund.eastmoney.com/519005.html"
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240"

with requests.request('GET',url,headers = {'User-agent':ua}) as res:
    content = res.text          #获取HTML的内容
    html = etree.HTML(content)  #分析HTML，返回DOM根节点
    orders = html.xpath("//div[@class='dataOfFund']//dl/span/text()")
    #print(orders)
    a=orders[0]
    b=orders[1]
    c=orders[2]

db = pymysql.connect(host='localhost', user='root', password='rkm2018', port=3306, db='stock')
cursor = db.cursor()
#sql = "insert into tb_fund (Codes,Sname,Vvalue,Vaddnu,Vaddpe) values('007244','安信核心混合C','{a}','{b}','{c}');"
sql = "insert into tb_fund_519005 (Codes,Sname,Vvalue,Vaddnu,Vaddpe) values('519005','海富通股票混合','%s','%s','%s');" %(a,b,c)
cursor.execute(sql)
db.commit()
cursor.close()
db.close()
