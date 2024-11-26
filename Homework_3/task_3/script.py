import requests
from bs4 import BeautifulSoup

url = 'https://stackoverflow.com/'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    title = soup.title.string
    print(f"Title of the page: {title}")
    
    links = soup.find_all('a')
    for link in links:
        print(link.get('href'))
else:
    print(f"Status code: {response.status_code}")
