from bs4 import BeautifulSoup
import requests

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'})

r = session.get('https://www.51voa.com/VOA60_1.html')

soup = BeautifulSoup(r.content.decode(), 'html.parser')
for li in soup.find(class_='list').find_all("li"):
    r = session.get('https://files.51voa.cn/v'+li.a['href'][11:-5]+'.mp4')
    print(li.contents[2][1:])
    with open('./download/'+ li.contents[2][1:] + li.a['href'][12:-11] + '.mp4','wb') as f:
        f.write(r.content)
