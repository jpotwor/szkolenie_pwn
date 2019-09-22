from project_imdb.imdb_manager.imdb_manager import ImdbManager
from project_imdb.imdb_manager.film import Person, Genre, Film
import bs4 as bs
import urllib.request
from project_imdb.config import host, user, password, db
imdb_manager = ImdbManager(host, user, password, db)

imdb_base_url = 'https://www.imdb.com'

film_rank_content = urllib.request.urlopen(imdb_base_url + '/chart/top?ref_=nv_mv_250').read()

film_rank_soup = bs.BeautifulSoup(film_rank_content, 'lxml')

movie_tds = film_rank_soup.findAll('td', {'class': 'titleColumn'})

movie_hrefs = []
for movie_td in movie_tds:
    movie_href = movie_td.find('a').attrs['href']
    movie_hrefs.append(imdb_base_url + movie_href)


for movie_href in movie_hrefs:
    film_detail_content = urllib.request.urlopen(movie_href).read()
    film_detail_content_soup = bs.BeautifulSoup(film_detail_content, 'lxml')
    title_wrapper_div = film_detail_content_soup.find('div', {'class': 'title_wrapper'})
    print('*')



