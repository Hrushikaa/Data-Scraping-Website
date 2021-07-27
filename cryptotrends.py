
from bs4 import BeautifulSoup as bs4
import requests
import pandas as pd


trend_name = []
count=[]
# twentyfourh =[]
# sevenday = []
marketcap = []
Volume =[]
CirculatingSupply=[]

page = requests.get('https://coinmarketcap.com/')
soup = bs4(page.text, 'html.parser')

for i in soup.find_all('p', class_ ="sc-1eb5slv-0 iJjGCS"):
    ttl = i.getText()
    trend_name.append(ttl)

for j in soup.find_all('div',  class_="sc-131di3y-0 cLgOOr"):
    cnt = j.getText()
    count.append(cnt)


# for j in soup.find_all('span',  class_="sc-15yy2pl-0 kAXKAX"):
#     tfh = j.getText()
#     twentyfourh.append(tfh)
# print(twentyfourh)
#
# for j in soup.find_all('span',  class_="sc-15yy2pl-0 hzgCfk"):
#     sd = j.getText()
#     sevenday.append(sd)
# print(sevenday)

for j in soup.find_all('span',  class_="sc-1ow4cwt-0 iosgXe"):
    mtc = j.getText()
    marketcap.append(mtc)


for j in soup.find_all('p',  class_="sc-1eb5slv-0 kDEzev font_weight_500___2Lmmi"):
    vl = j.getText()
    Volume.append(vl)



for j in soup.find_all('p',  class_="sc-1eb5slv-0 hNpJqV"):
    cs = j.getText()
    CirculatingSupply.append(cs)


data = {'Name': trend_name, 'Price': count,  'Market Cap': marketcap, 'Volume(24h)': Volume, 'Circulating Supply': CirculatingSupply}
df = pd.DataFrame(data=data)
# df.index+=1

df.to_csv('cryptoutput.csv', encoding='latin1', index=False)

file = pd.read_csv("cryptoutput.csv")
file.to_html("merger/cryptindex.html", index=False)
