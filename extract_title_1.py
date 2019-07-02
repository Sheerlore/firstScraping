import sys
import requests
from bs4 import BeautifulSoup
import datetime
import csv


#検索キーワード
list_keywd = ['python']
#検索数
search_num = 10
#GoogleのURL
search_URL = 'https://www.google.co.jp/search?num='+ str(search_num)
#User-Agent
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36 "}


if list_keywd:
    #Googleに接続
    request_Google = requests.get(search_URL, params={'q':' '.join(list_keywd) },headers = headers)
    request_Google.raise_for_status()

    #BeautifulSoupで掲載サイトのURLを取得
    bs4_Google = BeautifulSoup(request_Google.text,"html.parser")


    #scriptタグを削除
    for script in bs4_Google.find_all('script',src = False):
        script.decompose()
    #styleタグを削除
    for style in bs4_Google.find_all('style',src = False):
        style.decompose()

    print(bs4_Google.prettify())

    #検索結果のタイトルを取得
    title = bs4_Google.find_all('h3',{'class':'LC20lb'})
    url = bs4_Google.find_all('cite',{'class':'iUh30'})

    #出力
    for (tl,ul) in zip(title, url) :
        print(" ・ " + tl.text)
        print("     <"+ ul.text+">")
        print("\n")
