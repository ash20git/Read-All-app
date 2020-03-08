import requests

from bs4 import BeautifulSoup

sports_category_list = ['cricket','tennis','football']

def cat_news():
    cnt = 0
    news_li = []
    url = 'https://www.tribuneindia.com/'

    page = requests.get(url)

    s = BeautifulSoup(page.text,'html.parser')

    item = s.find_all('a', class_='card-top-align')

    for i in item:
        cnt+=1
        if cnt>12:
            break
        i= i.text.strip()
        news_li.append(i)

    
    # print(item)
    return news_li


def cat_sports(x):

    num=1
    sports_x = []

    if x in sports_category_list:
        url = 'https://indianexpress.com/section/sports/' + str(x) + '/'  
    else:
        return "ERROR IN SCRAPING"


    page = requests.get(url)

    soup = BeautifulSoup(page.text,'html.parser')

    base = soup.find_all('div',class_='articles')

    for b in base:
        num+=1
        if num>15:
            break
        item = b.find('h2',class_='title')
        item = item.text
        sports_x.append(item)

    return sports_x


def top_story_home():

    url = 'https://www.hindustantimes.com/top-news/'

    page = requests.get(url)

    img_found = BeautifulSoup(page.text,'html.parser')
    
    img_found = img_found.find('img', class_='img-responsive')

    img_text = img_found['title']

    img_href = img_found['data-src']

    return img_text, img_href

def img_coll():
    cnt=0
    img_href = []
    img_text = []
    url = 'https://www.hindustantimes.com/top-news/'

    page = requests.get(url)

    obj = BeautifulSoup(page.text,'html.parser')

    img = obj.find_all('div', class_='relative-icons')

    for i in img:
        cnt+=1
        if cnt>4:
            break

        i=i.find('img')
        img_href.append(i['src'])
        img_text.append(i['title'])


    x = list(zip(img_href,img_text))

    return x


