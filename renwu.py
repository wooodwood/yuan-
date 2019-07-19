import requests
import re
import os
import random
import urllib.request
proxier=[
    {'http': 'http://60.246.89.102:53281'},
    {'http': 'http://39.96.63.240:80'},
    {'http': 'http://43.240.5.178:53281'},
    {'http': 'http://39.96.63.240:80'},
    {'http': 'http://117.190.90.20:8060'},
    {'http': 'http://116.114.19.211:443'},
    {'http': 'http://116.113.27.170:61825'},
    {'http': 'http://118.24.128.46:1080'}
]
def init(folder):
    os.mkdir(folder)
    os.chdir(folder)
def singlepage(id,folder):
    url="http://www.gaoyuanlight.com/api/goods/describe"
    dat = {
        'id': str(id),
        'token': '',
        'client': 'pc_web',
        'version': '1.0',
        'location': '2,52,500'
    }
    print(str(id)+'\n')
    header = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '63',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        #'Cookie': 'PHPSESSID=50svt4t2ap8u3fu4jmni…aditionZeroStockBuy%22%3A0%7D',
        'Host': 'www.gaoyuanlight.com',
        'Referer': 'http://www.gaoyuanlight.com/goods?id='+str(id),
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
        'X-Requested-With': 'XMLHttpRequest'
    }
    try:
        proxiertemp = random.choice(proxier)
        html = requests.post(url, data=dat, headers=header, proxies=proxiertemp)
        print(html.json())
        msglist=html.json()['result']['attrs']
        with open(folder,'a+') as f:
            for i in range(len(msglist)):
                f.write(msglist[i]['name']+':'+msglist[i]['val']+'\n')
            f.write('\n')
    except Exception as e:
        with open(folder,'a+')as f:
            f.write("商品id="+str(id)+'爬取代理错误:'+'\n')
            f.write(str(e)+'\n\n')
            print(e)

def main(folder='hh'):
    init(folder)
    url='http://www.gaoyuanlight.com/search/searchList'
    header={
    'Accept':'application/json, text/javascript, */*; q=0.01,',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection':'keep-alive',
    'Content-Length':'109',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie':'PHPSESSID=50svt4t2ap8u3fu4jmnif28b85',
    'Host':'www.gaoyuanlight.com',
    'Referer':'http://www.gaoyuanlight.com/search?act=index&tab=1&tdsourcetag=s_pctim_aiomsg',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
    'X-Requested-With':'XMLHttpRequest'
    }
    dat={
    'page':'1',
    'pageSize':'20',
    'brand':'',
    'attrs':'',
    'coupon':'',
    'tab':'1',
    'kw':'',
    'by':'',
    'token':'',
    'client':'pc_web',
    'version':'1.0',
    'location':'2,52,500'
    }
    try:
        proxiertemp=random.choice(proxier)
        html=requests.post(url,data=dat,headers=header,proxies=proxiertemp)
       # print(html.json()['result']['list'])
        for n in range(20):
            singlepage(html.json()['result']['list'][n]['skus'][0]['id'],folder)
    except Exception as e:
        print(e)
if __name__=='__main__':
    main()