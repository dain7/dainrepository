from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from selenium import webdriver

import pandas as pd
import numpy as np
import csv



baseUrl = 'https://www.pinterest.co.kr/search/pins/?q='
plusUrl = input('검색어 입력: ')
crawl_num = int(input('크롤링할 갯수 입력(최대 50개): '))
url = baseUrl + plusUrl

browser = webdriver.Chrome()
browser.get(url)
ret = browser.page_source
soup = bs(ret, "html.parser")
soup
img = soup.find_all('img')




place_df2 = place_df.loc[df['address'].str.contains(area, na=False)]
place_df3 = place_df2.loc[df['title'].str.contains(search, na=False)]

n=1
for i in img:
    print(n)
    imgUrl = i['src']
    with urlopen(imgUrl) as f:
        with open('./images/img' + str(n) + '.jpg', 'wb') as h:
            img = f.read()
            h.write(img)

    n += 1
    if n > crawl_num:
        break

print('Image Crawling is done.')


#----------------------------------------------------------
import requests

number = request.form['number']



baseUrl = 'https://www.pinterest.co.kr/search/pins/?q='
url = baseUrl + 'solo' + 'photoshoot'
browser = webdriver.Chrome()
browser.get(url)
ret = browser.page_source
soup = bs(ret, "html.parser")
img = soup.find_all('img')
img
n=1
img_list = []
for i in img:
    imgUrl = i['src']
    img_list.append(imgUrl)

img_list


#-----------------------------------------------------------------
#
#                         명소정보 크롤링
#
#-----------------------------------------------------------------

browser = webdriver.Chrome()
browser.get('https://map.naver.com/v5/search/%EB%B6%80%EC%82%B0%20%EA%B0%80%EB%B3%BC%EB%A7%8C%ED%95%9C%20%EA%B3%B3?c=14365465.2176878,4186420.2093221,14,0,0,0,dh')
ret = browser.page_source
soup = bs(ret, "html.parser")

title = soup.select('span.search_title_text')
address = soup.select('div > div.search_box > div:nth-child(3) > span')
img = soup.select('div.link_search > a > img')

title_list = []
for i in title:
    a = i.text
    title_list.append(a)

address_list = []
for i in address:
    a = i.text
    address_list.append(a)

img_list = []
for i in img:
    imgUrl = i['src']
    img_list.append(imgUrl)


all_list = []
for a,b,c in zip(title_list, address_list, img_list):
    all_list.append([a, b, c])

all_list


df = pd.DataFrame(all_list)
df.columns = ['title', 'address', 'imgurl']
df.to_excel('place2.xlsx', index=False)
df




#---------------------------------------
#
#
#          카테고리 만들기
#
#---------------------------------------

place_df = pd.read_excel('./place.xlsx')

# 검색 값을 i로 받음
df2 = place_df.loc[place_df['address'].str.contains('서울', na=False)]
place_df3 = place_df.loc[place_df['title'].str.contains('공원', na=False)]
place_df3
#df2에 있는 것들을 랜덤으로 뽑아주기
place_list = place_df3.values.tolist()
place_list

import random

out = random.sample(df_list, 2)
print(out)

#--------------------------------
#
#
#        엑셀 읽기
#
#---------------------------------


xlsx = pd.read_excel('./place.xlsx')
