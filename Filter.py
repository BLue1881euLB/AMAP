# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 15:34:04 2018

@author: 24127
"""

import pandas as pd
import jieba
keyword = {
           'PEACEBIRD MEN':['peacebirdmen','太平鸟男装','太平鸟风尚男装'],
           'PEACEBIRD WOMEN':['peacebirdwomen','太平鸟女装'],
           'LEDIN':['ledin','乐町'],
           'MINI PEACE':['minipeace','太平鸟童装'],
           'MATERIAL GIRL':['materialgirl']}
keyword1 = {'凯胜':['羽毛球','kason','凯胜体育','凯胜足球'],'红双喜':['红双喜','乒乓球','红双喜专柜'],
            'DANSKIN':['danskin'],'AIGLE':['aigle','艾高专柜'],'lotto':['lotto'],
            'YoungLining':['李宁kids','李宁儿童','李宁童装','younglining','liningkids']
        } 
type1 = {'凯胜':['体育用品店','专营店','购物服务'],'红双喜':['体育用品店'],
            'DANSKIN':['danskin'],'AIGLE':['品牌服装店','专营店','体育用品店'],'lotto':['专卖店','购物服务'],
            'YoungLining':['李宁专卖店','专营店','专卖店','儿童用品店','体育用品店','购物相关场所']
        }
keyword2 = {'La Chapelle HOMME':['lachapellehomme','拉夏贝尔男装'],
            'La Chapelle SPORT':['lachapellesport','lachapellesports'],
            'La Chapelle Kids':['lachepellekids'],'POTE':['pote','pt','potevougeek'],'7.Modifier':['莫丽菲尔','modifier','7m'],
            "Candie's":['candies'],'LaBabite':['lababite','拉贝缇'],'Vougeek':['vougeek'],'Puella':['puella']
        }
peak = ['匹克','peak','thepeak','匹克体育','匹克运动','匹克专柜','匹克专营店']
type_peak = ['体育用品店','购物相关场所','专营店','专卖店']

jieba.suggest_freq('太平鸟男装',tune=True)
jieba.suggest_freq('太平鸟风尚男装',tune=True)
jieba.suggest_freq('太平鸟女装',tune=True)
jieba.suggest_freq('太平鸟童装',tune=True)
jieba.suggest_freq('乐町',tune=True)
jieba.suggest_freq('拉夏贝尔男装',tune=True)
jieba.suggest_freq('莫丽菲尔',tune=True)
jieba.suggest_freq('拉夏贝尔',tune=True)
jieba.suggest_freq('7m',tune=True)
jieba.suggest_freq('凯胜体育',tune=True)
jieba.suggest_freq('凯胜足球',tune=True)
jieba.suggest_freq('红双喜专柜',tune=True)
jieba.suggest_freq('艾高专柜',tune=True)
jieba.suggest_freq('红双喜',tune=True)
jieba.suggest_freq('李宁kids',tune=True)
jieba.suggest_freq('李宁儿童',tune=True)
jieba.suggest_freq('李宁童装',tune=True)
jieba.suggest_freq('young李宁',tune=True)
jieba.suggest_freq('李宁young',tune=True)
jieba.suggest_freq('匹克体育',tune=True)
jieba.suggest_freq('匹克运动',tune=True)
jieba.suggest_freq('匹克鞋店',tune=True)
jieba.suggest_freq('匹克专柜',tune=True)
jieba.suggest_freq('匹克专营店',tune=True)
jieba.suggest_freq('艾斯匹克',tune=True)
jieba.suggest_freq('奥林匹克',tune=True)
jieba.suggest_freq('艾诺丝雅诗',tune=True)
jieba.suggest_freq('岁月如歌',tune=True)
jieba.suggest_freq('匹克',tune=True)
jieba.del_word('一百匹')
def Filter_Peacebird():
    data = pd.read_csv('Amap Peace bird Sub.csv',encoding='utf_8',index_col=0)
    data.index = list(range(data.shape[0]))
    BigShop = pd.read_csv('Amap 太平鸟.csv',index_col=0)
    BigShop.drop_duplicates('id','first',inplace=True)
    namelist = list(data['name'])
    delete = []
    indexlist = list(data.index)
    for i,name in zip(indexlist,namelist):
        keyname = ','.join(jieba.cut(data.loc[i]['name'].replace(' ','').replace("'",'').lower())).split(',')
        print(keyname)
        temp = 0
        for word in keyname:
            if word in keyword[data.loc[i]['brand']]:
                temp = 1
                break
        if temp:
            pass
        else:
            delete.append(i)
    data.drop(delete,inplace=True)
    data.drop_duplicates(['id','brand'],'first',inplace=True)
    data1 = data.append(BigShop)
    data1.drop_duplicates('id','first',inplace=True)
    
    data1.to_csv('太平鸟.csv')
    return data1
    pass

def Filter_LaChapelle():
    data = pd.read_csv('Amap La Chapelle Sub.csv',encoding='utf_8',index_col=0)
    data.index = list(range(data.shape[0]))
    BigShop = pd.read_csv('Amap La Chapelle.csv',index_col=0)
    BigShop.drop_duplicates('id','first',inplace=True)
    delete = []
    namelist = list(data['name'])
    indexlist = list(data.index)
    for i,name in zip(indexlist,namelist):
        keyname = ','.join(jieba.cut(data.loc[i]['name'].replace(' ','').replace("'",'').lower())).split(',')
        print(keyname)
        temp = 0
        for word in keyname:
            if word in keyword2[data.loc[i]['brand']]:
                temp = 1
                break
        if temp:
            pass
        else:
            delete.append(i)
    data.drop(delete,inplace=True)
    data.drop_duplicates(['id','brand'],'first',inplace=True)
    
    lachapelle = ['拉夏贝尔','拉夏贝儿','lachapelle','candies','lababite','拉贝缇','vougeek','puella']
    delete = []
    namelist = list(BigShop['name'])
    indexlist = list(BigShop.index)
    for i,name in zip(indexlist,namelist):
        keyname = ','.join(jieba.cut(BigShop.loc[i]['name'].replace(' ','').replace("'",'').replace('·','').lower())).split(',')
        print(keyname)
        temp = 0
        for word in keyname:
            if word in lachapelle:
                for word in BigShop.loc[i]['Type'].split(';'):
                        temp = 1
                        break
            
            else:
                pass
        if temp:
            pass
        else:
            delete.append(i)    
    BigShop.drop(delete,inplace=True)
    namelist = list(BigShop['name'])
    indexlist = list(BigShop.index)
    for i,name in zip(indexlist,namelist):
        keyname = ','.join(jieba.cut(BigShop.loc[i]['name'].replace(' ','').replace("'",'').replace('·','').lower())).split(',')
        for word in keyname:
            for Key in keyword2:
                if word in keyword2[Key]:
                    BigShop.loc[i,'brand'] = Key
 
   
    data1 = data.append(BigShop)
    data1.drop_duplicates('id','first',inplace=True)
    data1 = data1.sort_index(by = ['brand','province','city','area'])    
    data1.to_csv('La Chapelle.csv')
    return data1

def Filter_Lining():
    data = pd.read_csv('Amap 李宁 Sub.csv',encoding='utf_8',index_col=0)
    data.index = list(range(data.shape[0]))
    BigShop = pd.read_csv('Amap 李宁.csv',index_col=0)
    BigShop.drop_duplicates('id','first',inplace=True)  
    delete = []
    namelist = list(data['name'])
    indexlist = list(data.index)
    for i,name in zip(indexlist,namelist):
        keyname = ','.join(jieba.cut(data.loc[i]['name'].replace(' ','').replace("'",'').replace('·','').replace('-','').lower())).split(',')
        print(keyname)
        temp = 0
        for word in keyname:
            if word in keyword1[data.loc[i]['brand']]:
                for word in data.loc[i]['Type'].split(';'):
                    if word in type1[data.loc[i]['brand']]:
                        temp = 1
                        break
            
            else:
                pass
        if temp:
            pass
        else:
            delete.append(i)
    data.drop(delete,inplace=True)
    data.drop([4808,5333],inplace=True)
    data.drop_duplicates(['id','brand'],'first',inplace=True)
    
    type_lining = ['体育用品店','李宁专卖店','专营店','专卖店','购物相关场所']
    lining = ['李宁','lining']    
    
    delete = []
    namelist = list(BigShop['name'])
    indexlist = list(BigShop.index)
    for i,name in zip(indexlist,namelist):
        keyname = ','.join(jieba.cut(BigShop.loc[i]['name'].replace(' ','').replace("'",'').replace('·','').lower())).split(',')
        print(keyname)
        temp = 0
        for word in keyname:
            if word in lining:
                for word in BigShop.loc[i]['Type'].split(';'):
                    if word in type_lining:
                        temp = 1
                        break
            
            else:
                pass
        if temp:
            pass
        else:
            delete.append(i)    
    
    BigShop.drop(delete,inplace=True)
    
    namelist = list(BigShop['name'])
    indexlist = list(BigShop.index)
    for i,name in zip(indexlist,namelist):
        keyname = ','.join(jieba.cut(BigShop.loc[i]['name'].replace(' ','').replace("'",'').replace('·','').lower())).split(',')
        for word in keyname:
            for Key in keyword1:
                if word in keyword1[Key]:
                    BigShop.loc[i,'brand'] = Key
    data1 = data.append(BigShop)
    data1.drop_duplicates('id','first',inplace=True)
    data1 = data1.sort_index(by = ['brand','province','city','area'])
    data1.to_csv('李宁.csv')
    return data1
    pass

def Filter_Peak():
    data = pd.read_csv('Amap 匹克peak.csv',index_col=0,encoding='utf_8')
    data['brand'] = '匹克'
    delete = []
    namelist = list(data['name'])
    indexlist = list(data.index)
    for i,name in zip(indexlist,namelist):
        keyname = ','.join(jieba.cut(data.loc[i]['name'].replace(' ','').replace("'",'').replace('·','').replace('-','').lower())).split(',')
        print(keyname)
        temp = 0
        for word in keyname:
            if word in peak:
                for Type in list(data.loc[i]['Type'].split(';')):
                    if Type in type_peak:
                        temp = 1
                        break
            else:
                pass
        if temp==0:
            delete.append(i)
    data.drop(delete,inplace=True)
    data.drop_duplicates('id',inplace=True)
    data.sort_index(by = ['brand','province','city','area'],inplace=True)
    data.to_csv('匹克.csv')
    return data
    pass

def Filter_MissLi():
    missli = ['missli']
    type_missli = ['品牌服装店','专卖店','专营店','服装鞋帽皮具店','购物相关场所']
    data = pd.read_csv('Amap MissLi.csv',index_col=0)
    delete = []
    namelist = list(data['name'])
    indexlist = list(data.index)
    for i,name in zip(indexlist,namelist):
        keyname = ','.join(jieba.cut(data.loc[i]['name'].replace(' ','').replace("'",'').replace('·','').replace('-','').lower())).split(',')
        print(keyname)
        temp = 0
        for word in keyname:
            if word in missli:
                for Type in list(data.loc[i]['Type'].split(';')):
                    if Type in type_missli:
                        temp = 1
                        break
            else:
                pass
        if temp==0:
            delete.append(i)
    data.drop(delete,inplace=True)
    data.drop_duplicates('id',inplace=True)
    data.sort_index(by = ['brand','province','city','area'],inplace=True)
    data.to_csv('MissLi.csv')
    return data
    pass    

def Filter_AiWei():
    Aiwei = {'ARIOSEYEARS|艾诺丝雅诗|艾诺丝·雅诗':['arioseyears','艾诺丝雅诗','艾诺丝','薆诺丝雅诗'],
             'SUIYUERUGE|岁月如歌':['岁月如歌','suiyueruge']}
    type_Aiwei = {'ARIOSEYEARS|艾诺丝雅诗|艾诺丝·雅诗':['品牌服装店','专营店','专卖店','购物相关场所','服装鞋帽皮具店'],
                  'SUIYUERUGE|岁月如歌':['品牌服装店','品牌鞋店','服装鞋帽皮具店','专卖店','专营店']}
    data = pd.read_csv('Amap 爱维服饰 Sub.csv',index_col=0)
    delete = []
    namelist = list(data['name'])
    indexlist = list(data.index)
    for i,name in zip(indexlist,namelist):
        keyname = ','.join(jieba.cut(data.loc[i]['name'].replace(' ','').replace("'",'').replace('·','').replace('-','').replace('&','').lower())).split(',')
        temp = 0
        for key in keyname:
            if key in Aiwei[data.loc[i,'brand']]:
                for Type in list(data.loc[i]['Type'].split(';')):
                    if Type in type_Aiwei[data.loc[i,'brand']]:
                        temp = 1
                        break
                    
        if temp==0:
            delete.append(i)
    
    data.drop(delete,inplace=True)
    data.drop_duplicates(['id','brand'],'first',inplace=True)
    data.sort_index(by = ['brand','province','city','area'],inplace=True)
    data.to_csv('爱维服饰.csv')
        
    
    pass

def Filter_Mall():
    type_mall = ['普通商场', '商场']
    mall = ['广场', '购物中心', '商城', '商厦', '座', '大厦']
    data = pd.read_csv('Amap shopping mall.csv', index_col=0)
    delete = []
    namelist = list(data['name'])
    indexlist = list(data.index)
    for i, name in zip(indexlist, namelist):
        temp = 0
        if '购物中心' in list(data.loc[i]['Type'].split(';')):
            temp = 1
        elif ('普通商场'in list(data.loc[i]['Type'].split(';')))|('商场'in list(data.loc[i]['Type'].split(';'))):
            keyname = ','.join(jieba.cut(data.loc[i]['name'].replace(' ', '').replace("'", '').replace('·', '').replace('-','').replace('&', '').lower())).split(',')
            for key in keyname:
                if key in mall:
                    temp = 1
                    break
        if temp == 0:
            delete.append(i)
    data.drop(delete,inplace=True)
    data.drop_duplicates(['id', 'brand'], 'first', inplace=True)
    data.sort_index(by=['brand', 'province', 'city', 'area'], inplace=True)
    data.index = list(range(1,data.shape[0]+1))
    data.to_csv('shopping mall.csv')
    pass



