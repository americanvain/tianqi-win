
#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import json


if __name__ =="__main__":
    header = {
        'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0'
    }
    url ='http://www.weather.com.cn/weather1d/101280101.shtml'

    html = requests.get(url= url,headers=header)
    html.encoding='utf-8'
    html_text=html.text

    obj2 = re.compile(r'{"od21".*?}')
    result2 = obj2.finditer(html_text)
    jieguo =''
    jieguo_list=[]
    for i in result2:
        jieguo =i.group()
        jieguo_list.append(json.loads(jieguo))


    
    print("finished")



    pass