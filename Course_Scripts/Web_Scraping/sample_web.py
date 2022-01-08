import requests
import bs4

result = requests.get('https://www.example.com')
soup = bs4.BeautifulSoup(result.text, 'lxml')
title = soup.select('title')[0].get_text()
para = soup.select('p')[0].get_text()
print(f'Title of the page: {title}')
print(f'Body of the page: {para}')

#GETTING THE IMAGE FORM WIKIPEDIA

req = requests.get('https://en.wikipedia.org/wiki/Vijay_(actor)')
soup = bs4.BeautifulSoup(req.text,'lxml')
image1 = soup.select('.image')[0]
image_link = requests.get('https:'+image1['src'])

f = open('new_image_file.jpg', 'wb')
f.write(image_link.content)
f.close()