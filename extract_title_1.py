import sys
import requests
from bs4 import BeautifulSoup
import datetime
import csv


#検索キーワード
list_keywd = ['python']
#検索数
search_num = 100
#GoogleのURL
search_URL = 'https://www.google.co.jp/search?num='+ str(search_num)

if list_keywd:
    #Googleに接続
    request_Google = requests.get(search_URL, params={'q':' '.join(list_keywd) })
    request_Google.raise_for_status()

    #BeautifulSoupで掲載サイトのURLを取得
    bs4_Google = BeautifulSoup(request_Google.text,"html.parser")

    #scriptタグを削除
    for script in bs4_Google.find_all('script',src = False):
        script.decompose()
    #styleタグを削除
    for style in bs4_Google.find_all('style',src = False):
        style.decompose()
    #print(bs4_Google.prettify())

    #検索結果のタイトルを取得
    title = bs4_Google.find_all('div',{'class':'BNeawe vvjwJb AP7Wnd'})

    #出力
    for index, tl in enumerate(title) :
        print(str(index)+ ": " + tl.text)
