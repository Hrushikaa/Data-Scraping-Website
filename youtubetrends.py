from bs4 import BeautifulSoup as bs4
import requests
import pandas as pd


trend_name = []
count=[]

page = requests.get('https://yt-trends.iamrohit.in/India')
soup = bs4(page.text, 'html.parser')
# for i in soup.find_all('tbody', id="copyData"):
for i in soup.find_all('a', class_="pl"):
    ttl = i.getText()
    # ttl = ttl.replace('Tweets', '')
    trend_name.append(ttl)


while(" " in trend_name) :
    trend_name.remove(" ")
while("[ReadMore..]" in trend_name):
    trend_name.remove("[ReadMore..]")
# print(trend_name)
#
for j in soup.find_all('p',style='color:green;'):

    cnt = j.getText()

    count.append(cnt)
# print(count)

data = {'Youtube trending': trend_name, 'Details': count}
df = pd.DataFrame(data=data)
df.index+=1
df.index.name = 'No.'
df.to_csv('ytoutput.csv', encoding='latin1')


file = pd.read_csv("ytoutput.csv")
file.to_html("merger/ytindex.html", index=False)


