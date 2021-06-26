from bs4 import BeautifulSoup
import requests

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'})

r = session.get('https://www.51voa.com/VOA60_1.html')

print(r.content.decode())
soup = BeautifulSoup(r.content.decode(), 'html.parser')
print(soup.find(class_='list'))
for li in soup.find(class_='list').find_all("li"):
    print(li)
    print(li.a['href'])