import requests
import bs4

base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
two_star_titles = []

for n in range(1,51):
    scrap_url = base_url.format(n)
    res = requests.get(scrap_url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    books = soup.select('.product_pod')

    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            book_title = book.select('a')[1]['title']
            two_star_titles.append(book_title)

print(f'Number of Two star rating books: {len(two_star_titles)}')
print('Title of the Books are, ')
for title in two_star_titles:
    print(title)

