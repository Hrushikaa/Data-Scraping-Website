
from bs4 import BeautifulSoup as bs4
import requests
import pandas as pd
# eel.init("web")
#
# @eel.expose
def scrap_twitter():
    trend_name = []
    count = []
    l=[]

    page = requests.get('https://twitter-trends.iamrohit.in/india')
    soup = bs4(page.text, 'html.parser')
    # for i in soup.find_all('tbody', id="copyData"):
    for i in soup.find_all('a', class_="tweet"):
        ttl = i.getText()
        # ttl = ttl.replace('Tweets', '')
        trend_name.append(ttl)

    for j in soup.find_all('span', class_="badge"):
        cnt = j.getText()
        # # ttl = ttl.replace('Tweets', '')
        count.append(cnt)

    for k in range(1,51):
        l.append(k)

    data = {'No.': l, 'Twitter Trending Hashtags': trend_name, 'Tweet Volume': count}
    df = pd.DataFrame(data=data)

    df.index+=1
    df.to_csv('df_output.csv', encoding='latin1', index=False)

    # df.to_excel("/Users/hrushika/Desktop/webscrap/output1.xlsx")
    # result = df.to_html()
    # print(result)
    # html = df.to_html()
    #
    # # write html to file
    # text_file = open("index10.html", "w")
    # text_file.write(html)
    # text_file.close()
    #
    # df.to_html(classes='table table-striped')

    file = pd.read_csv("df_output.csv")
    file.to_html("merger/index10.html", index=False)



scrap_twitter()
