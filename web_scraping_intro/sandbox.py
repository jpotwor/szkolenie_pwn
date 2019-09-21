import urllib.request
import bs4 as bs

imdb_base_url = 'https://www.imdb.com'

film_rank_content = urllib.request.urlopen(imdb_base_url + '/chart/top?ref_=nv_mv_250').read()

film_rank_soup = bs.BeautifulSoup(film_rank_content, 'lxml')

movie_tds = film_rank_soup.findAll('td', {'class': 'titleColumn'})

movie_hrefs = []
for movie_td in movie_tds:
    movie_href = movie_td.find('a').attrs['href']
    movie_hrefs.append(imdb_base_url + movie_href)

print(movie_hrefs)

for movie_href in movie_hrefs:
    print(movie_href)