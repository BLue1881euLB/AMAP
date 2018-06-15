# -*- coding: utf-8 -*-
# """
# Created on Thu Jun  7 22:48:58 2018
#
# @author: QF
# """

import requests
import json
import pandas as pd
import time

city = pd.read_excel('C:/Users/24127/OneDrive/AMAP/data/AMap_adcode_citycode.xlsx',dtype=str)
city_code = list(set(city['citycode']))
keywordlist = ['李宁','太平鸟','La Chapelle','爱维服饰']
subshop = {'李宁':['凯胜','红双喜','DANSKIN','AIGLE','lotto'],
           '太平鸟':['PEACEBIRD MEN','PEACEBIRD WOMEN','LEDIN','MINI PEACE','MATERIAL GIRL'],
           'La Chapelle':['La Chapelle HOMME','La Chapelle SPORT','La Chapelle Kids','POTE','7.Modifier',"Candie's",'LaBabite'],
           '爱维服饰':['ARIOSEYEARS|艾诺丝雅诗|艾诺丝·雅诗','SUIYUERUGE|岁月如歌']}

def getjson(palace,keyword,page_num=0):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    }
    url='http://restapi.amap.com/v3/place/text?'
    params={
        'keywords':keyword,
        'city':palace,
        'offset':'20',
        'page_size':'20',
        'page':page_num,
        'output':'json',
        'key':'65a4b70703b9ecc4f6ebd45e170ed712',
        'extensions':'all'
    }
    response=requests.get(url=url,params=params,headers=headers)
    html=response.text
    decodejson=json.loads(html)
    return decodejson

cols = ['brand','province','city','area','name','address','lat','lng','Type','id']
def GetShopMap(keyword):
    res = pd.DataFrame(columns=cols)
    res = res[cols]
    for city_No in city_code:
        not_last_page=True
        page_num=0
        while not_last_page:
            try:
                decodejson=getjson(city_No,keyword,page_num)
                time.sleep(1)
                print(city_No,page_num)
#            try:
                if decodejson.get('pois'):
                
                    for result in decodejson.get('pois'):
                        print(result)
                        if(len(result)>2):
                            shop=result['name']
                            cityname = result['cityname']
                            lat=result['location'].split(',')[1]
                            lng=result['location'].split(',')[0]
                            address=str(result['adname']) + str(result['address'])
                            Type=result['type']
                            province = result['pname']
                            area = result['adname']
                            ID = result['id']
                            res.loc[res.shape[0]]=[keyword,province,cityname,area,shop,address,lat,lng,Type,ID]
                      
                          
                    page_num=page_num+1
                    time.sleep(1)
                else:
                    not_last_page=False
            except:
                    continue
    keyword = keyword.replace('|','')
    res.to_csv('Amap'+' '+keyword+'.csv')

def GetSubShopMap(Sublist,brand):
    res = pd.DataFrame(columns=cols)
    res = res[cols]
    for subbrand in Sublist:
        for city_No in city_code:
            not_last_page=True
            page_num=0
            while not_last_page:
                try:
                    decodejson=getjson(city_No,subbrand,page_num)
                    time.sleep(1)
                    print(city_No,page_num)
#            try:
                    if decodejson.get('pois'):
                
                        for result in decodejson.get('pois'):
                            print(result)
                            if(len(result)>2):
                                shop=result['name']
                                cityname = result['cityname']
                                lat=result['location'].split(',')[1]
                                lng=result['location'].split(',')[0]
                                address=str(result['adname']) + str(result['address'])
                                Type=result['type']
                                province = result['pname']
                                area = result['adname']
                                ID = result['id']
                                res.loc[res.shape[0]]=[subbrand,province,cityname,area,shop,address,lat,lng,Type,ID]
                      
                          
                            page_num=page_num+1
                            time.sleep(1)
                    else:
                        not_last_page=False
                except:
                    continue
        res.to_csv('Amap'+' '+brand+' Sub'+'.csv')
    
    pass