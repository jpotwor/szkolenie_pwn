import pymysql
import bs4 as bs
import urllib.request


base_url = 'https://www.imdb.com'

film_rank_content = urllib.request.urlopen(base_url + '/chart/top?ref_=nv_mv_250').read()

film_rank_soup = bs.BeautifulSoup(film_rank_content, 'lxml')

movie_tds = film_rank_soup.findAll('td', {'class': 'titleColumn'})


for movie_td in movie_tds:

    conn = pymysql.connect(host='localhost', user='jan', password='jan_pass', charset='utf8')
    c = conn.cursor()
    c.execute('use imdb;')
    c.execute("SET NAMES 'UTF8';")
    c.execute("SET CHARACTER SET utf8;")
    movie_detail_link = base_url + movie_td.find('a').attrs['href']
    film_detail_content = urllib.request.urlopen(movie_detail_link).read()
    film_detail_soup = bs.BeautifulSoup(film_detail_content, 'lxml')

    movie = {}
    movie['title'] = film_detail_soup.findAll('h1')[0].text.split('\xa0')[0]
    movie['year'] = film_detail_soup.findAll('h1')[0].text.split('\xa0')[1]

    subtext = [el.strip() for el in film_detail_soup.findAll('div', {'class': 'subtext'})[0].text.split('|')]
    movie['genre'] = subtext[2].replace('\n', '')
    movie['duration'] = subtext[1]
    movie['rating_value'] = film_detail_soup.findAll('span', {'itemprop': 'ratingValue'})[0].text

    c.execute("INSERT INTO movies VALUES(NULL, '%s', '%s', '%s', '%s', '%s')" % (movie['title'], movie['year'], movie['genre'], movie['duration'], movie['rating_value']))
    conn.commit()

    print(movie)

conn.close()





