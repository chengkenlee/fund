#!/usr/bin/env python
"""
# Author: chenglee
# Created Time : Tue 14 Jan 2020 08:16:54 PM CST
# File Name: ji.py
# Description:
"""
# -*- coding:utf-8 -*-
# url:http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code=519005&sdate=2020-01-01&edate=2020-01-15&per=20
import sys 
import requests
from bs4 import BeautifulSoup
from prettytable import *
 
 
def get_url(url, params=None, proxies=None):
    rsp = requests.get(url, params=params, proxies=proxies)
    rsp.raise_for_status()
    return rsp.text
 
 
def get_fund_data(code, start='', end=''):
    record = {'Code': code}
    url = 'http://fund.eastmoney.com/f10/F10DataApi.aspx'
    params = {'type': 'lsjz', 'code': code, 'page': 1, 'per': 65535, 'sdate': start, 'edate': end}
    html = get_url(url, params)
    soup = BeautifulSoup(html, 'html.parser')
    records = []
    tab = soup.findAll('tbody')[0]
    for tr in tab.findAll('tr'):
        if tr.findAll('td') and len((tr.findAll('td'))) == 7:
            record['Date'] = str(tr.select('td:nth-of-type(1)')[0].getText().strip())
            record['NetAssetValue'] = str(tr.select('td:nth-of-type(2)')[0].getText().strip())
            record['ChangePercent'] = str(tr.select('td:nth-of-type(4)')[0].getText().strip())
            records.append(record.copy())
    return records
 
 
def demo(code, start, end):
    table = PrettyTable()
    table.field_names = ['Code', 'Date', 'NAV', 'Change']
    table.align['Change'] = 'r'
    records = get_fund_data(code, start, end)
    for record in records:
        table.add_row([record['Code'], record['Date'], record['NetAssetValue'], record['ChangePercent']])
    return table
 
 
if __name__ == "__main__":
    #print(demo(sys.argv[1], sys.argv[2], sys.argv[3]))
    print(demo('519005', '2020-03-17', '2020-03-21'))
