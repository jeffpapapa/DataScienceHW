# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 10:33:50 2018

@author: jeff
#1992-2340
第四部份split 用--分 join 1:
"""
import time
import requests
import re
from bs4 import BeautifulSoup
start = time.time()
now_page = 1992
f = open('1.txt', 'w', encoding = 'UTF-8')
ff = open('2.txt', 'w', encoding = 'UTF-8')
while(now_page <= 2340):
    url = "https://www.ptt.cc/bbs/Beauty/index" + str(now_page)+".html"
    #url = "https://www.ptt.cc/bbs/Beauty/index1992.html"
    r = requests.get(url)
    content = r.text
    
    soup = BeautifulSoup(content,"html.parser")
    
    title_list = soup.find_all(class_="r-ent")
    
    #print(title_list)
    
    for a_list in title_list:
        check = 0
        a_crash = a_list.find(class_="hl f1")
        #print(a_crash.string)
        
        if(a_crash != None):
            print(a_crash.string)
            check = 1
            
        a_title = a_list.find('a')
        if(a_title != None):
            now_title = a_title.string
            a_date = a_list.find(class_="date")
            now_date = a_date.string
            now_url = a_title.get('href')
            now_date = re.sub('/','',now_date)
            
            #print(now_date,',',now_title,',',now_url)
            if((now_page == 1992)and(int(now_date)==1231)):
                a=0
            elif((now_page == 2340)and(int(now_date)==101)):
                a=0
            else:
                print(now_date)
                f.write('{0},{1},{2}\n'.format(now_date,now_title,now_url))
                if(check == 1):
                    #print(now_date,',',now_title,',',now_url)
                    ff.write('{0},{1},{2}\n'.format(now_date,now_title,now_url))
                #f.write(now_date,',',now_title,',',now_url,'\n')
                #print(now_title)
                #print(now_url)
    now_page = now_page + 1
    time.sleep(2)
end = time.time()
print((end-start)," seconds")