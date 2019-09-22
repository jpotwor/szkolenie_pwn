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
    film_detail_soup = bs.BeautifulSoup(film_detail_content, 'lxml')

    # tile, year
    title_wrapper_div = film_detail_soup.find('div', {'class': 'title_wrapper'})
    year = title_wrapper_div.find('h1').find('span').find('a').text
    title = title_wrapper_div.find('h1').text
    title = title.replace('(%s)' % year, '').strip()


    credit_summary_items = film_detail_soup.findAll('div', {'class': 'credit_summary_item'})
    for credit_summary_item in credit_summary_items:
        # director
        if 'Director' in credit_summary_item.find('h4').text:
            director = credit_summary_item.find('a').text
            director_split = director.split(' ')
            first_name = director_split[0]
            last_name = director_split[-1]
            director = Person(first_name, last_name)

        # actors
        actors = []
        if 'Stars' in credit_summary_item.find('h4').text:
            for a in credit_summary_item.findAll('a'):
                if not 'full cast' in a.text:
                    a_split = a.text.split(' ')
                    first_name = a_split[0]
                    last_name = a_split[-1]
                    actor = Person(first_name, last_name)
                    actors.append(actor)

    print("title: '%s'; year: '%s; director: %s'; actors: %s" % (title, year, director, actors))







