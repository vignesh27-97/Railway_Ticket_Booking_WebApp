import requests
import bs4

base_url = 'http://quotes.toscrape.com/page/'
page_still_valid = True
authors_list = []
page = 1

while page_still_valid:
    page_url = base_url+str(page)
    res = requests.get(page_url)

    if "No quotes found!" in res.text:
        page_still_valid = False
        break

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    for name in soup.select('.author'):
        authors_list.append(name.text)

    page += 1

print('Authors List:')
for author in authors_list:
    print(author)

