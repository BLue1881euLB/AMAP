import pandas as pd
import jieba
import amap1
import numpy as np
from math import radians, cos, sin, asin, sqrt
mall_num = 0
def haversine(lon1, lat1, lon2, lat2):  # 经度1，纬度1，经度2，纬度2 （十进制度数）
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # 地球平均半径，单位为公里
    return c * r * 1000

def brand_mall():
    peacebird = pd.read_csv('C:/Users/24127/OneDrive/AMAP/data/peacebird.csv',index_col=0)
    lining = pd.read_csv('C:/Users/24127/OneDrive/AMAP/data/lining.csv',index_col=0)
    lachapella = pd.read_csv('C:/Users/24127/OneDrive/AMAP/data/La Chapelle.csv',index_col=0)
    missli = pd.read_csv('C:/Users/24127/OneDrive/AMAP/data/MissLi.csv',index_col=0)
    aiwei = pd.read_csv('C:/Users/24127/OneDrive/AMAP/data/aiwei.csv',index_col=0)
    peak = pd.read_csv('C:/Users/24127/OneDrive/AMAP/data/peak.csv',index_col=0)
    data = peacebird.append(lining,ignore_index=True)
    data = data.append(lachapella,ignore_index=True)
    data = data.append(missli,ignore_index=True)
    data = data.append(aiwei,ignore_index=True)
    shop = data.append(peak,ignore_index=True)
    mall = pd.read_csv('shopping mall.csv',index_col=0)
    mall.index = list(range(1,mall.shape[0]+1))

    shop.sort_index(by=['province','city','area','brand'],inplace=True)
    #print(shop)
    for province in list(set(shop['province'])):
        p = shop[shop['province']==province]
        for city in list(set(p['city'])):
            c = p[p['city']==city]
            for area in list(set(c['area'])):
                data1 = shop[(shop['province']==province)&(shop['city']==city)&(shop['area']==area)]
                data2 = mall[(mall['province']==province)&(mall['city']==city)&(mall['area']==area)]
                print(province,city,area)
                if (data1.shape[0]>0)&(data2.shape[0]>0):
                    mall_id,mall_name,mall = Judge_In(data1,data2,mall)
                #print(mall_id,mall_name)
                    shop.loc[data1.index,'mall_id'] = mall_id
                    shop.loc[data1.index,'mall_name'] = mall_name
                else:
                    for k in list(data1.index):
                        shop.loc[k, 'mall_id'] = 0
                        shop.loc[k,'mall_id'] = 'Nothing'
    shop.sort_index(by=['brand','province','city','area'],inplace=True)
    shop.to_csv('shop.csv')

def Judge_In(data1,data2,mall):
    mall_key = ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', '层', 'B1', 'B2', 'B3']
    mall_id = []
    mall_name = []
    print(data1.shape,data2.shape)
    for i in range(data1.shape[0]):
        temp = 0
        for j in range(data2.shape[0]):
            if haversine(data1.iloc[i]['lng'],data1.iloc[i]['lat'],data2.iloc[j]['lng'],data2.iloc[j]['lat']) < 1000:
                if Judege_Str(data1.iloc[i]['address'],data2.iloc[j]['name']):
                    mall_id.append(data2.index[j])
                    mall_name.append(data2.iloc[j]['name'])
                    print(mall_id[-1],mall_name[-1])
                    temp = 1
                    break

        if temp == 0:
            for word in ','.join(jieba.cut(data1.iloc[i]['address'])).split(','):
                if word in mall_key:
                    temp = 2
                    mall_id.append(mall.shape[0]+1)
                    mall_name.append(data1.iloc[i]['address'])
                    mall.loc[mall.shape[0]] = data1.iloc[i]
                    mall.loc[mall.shape[0],'brand'] = 'shopping mall'
                    break
        if temp == 0:
            mall_id.append(0)
            mall_name.append('Nothing')
    return mall_id,mall_name,mall

def Judege_Str(str1,str2):
    count = 0

    for word in ','.join(jieba.cut(str2.replace('(','').replace(')',''))).split(','):
        if word in str1:
            count +=1
    if count>1:
        return  True
    else:
        return False