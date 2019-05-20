import requests
import bs4

# GET

resp = requests.get('http://finance.naver.com/')
resp.raise_for_status()
resp.encoding = 'euc-kr'
html = resp.text
bs = bs4.BeautifulSoup(html, 'html.parser')
tags = bs.select('div.section_strategy ul li span a')  # Top news
title = tags[0].getText()
print(title)
