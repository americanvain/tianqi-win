
#-*- coding:utf-8 -*-

from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
import re
import json
import excl_test

def pipei(ori_text):
    obj = re.compile(r'{"od0":"(?P<date>\d+)"')
    date = obj.findall(ori_text)
    date_text=str(date[0])
    fp =open('./original_data/tianqidata'+date_text+'.txt','w',encoding='utf-8')
    fp.write(date_text+':\n')

    obj2 = re.compile(r'{"od21".*?}')
    result2 = obj2.finditer(ori_text)
    jieguo =''
    jieguo_list=[]
    for i in result2:
        jieguo =i.group()
        jieguo_list.append(json.loads(jieguo))

    tem_list=[]
    kongqizhiliang=[]
    xiangduishidu=[]
    fengli=[]
    time_list=[]
    right_now_time=datetime.strptime(date_text,'%Y%m%d%H%M')
    for i in jieguo_list:
        right_now_time=right_now_time-timedelta(hours=1)
        time_list.append(str(right_now_time))
        tem_list.append(i['od22'])
        kongqizhiliang.append(i['od28'])
        xiangduishidu.append(i['od27'])
        fengli.append(str(i['od24'])+str(i['od25'])+'级')
        fp.write(str(right_now_time))
        fp.write(i['od22']+' ')
        fp.write(i['od28']+' ')
        fp.write(i['od27']+' ')
        fp.write(i['od24']+i['od25']+'级'+' ')

    excl_test.excel_process(jieguo_list,right_now_time)

    # excl_test.excel_process(time_list,tem_list,kongqizhiliang,xiangduishidu,fengli)
    fp.close()
    pass


if __name__ =="__main__":
    excl_test.excel_creat()
    header = {
        'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0'
    }
    url ='http://www.weather.com.cn/weather1d/101280101.shtml'

    html = requests.get(url= url,headers=header)
    html.encoding='utf-8'
    html_text=html.text

    pipei(html_text)
    print("finished")



    pass