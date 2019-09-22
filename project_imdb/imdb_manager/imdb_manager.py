import pymysql
from project_imdb.config import host, user, password, db
from project_imdb.imdb_manager.imdb_queries import add_person_query, get_person_id_query, add_genre_query, \
    get_genre_id_query, add_film_row_query, add_actor_in_film_row, add_film_has_genre_row
from project_imdb.imdb_manager.film import Film


class Person:
    """
    Holds data about person
    """
    def __init__(self, first_name, last_name, nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.nationality = nationality


class Genre:
    """
    Holds data about genre
    """
    def __init__(self, name):
        self.name = name


class ImdbManager:

    def __init__(self, host, user, password, db):
        """
        class constructor:
        -) connect to DB
        """
        self.conn = pymysql.connect(host=host, user=user, password=password, charset='utf8', db=db)

    def _addPerson(self, person, table):
        """
        adds person to  table given person object,
        private method used by addActor and addDirector
        :param person: person object
        :param table: target table
        :return:
        """
        cursor = self.conn.cursor()
        print(add_person_query % (table, person.first_name, person.last_name, person.nationality))
        cursor.execute(add_person_query % (table, person.first_name, person.last_name, person.nationality))
        self.conn.commit()
        return self._getPersonId(person, table)

    def addActor(self, person):
        """
        adds person to actor table given person object
        :param person: person object
        :return: id in actor table
        """
        return self._addPerson(person, 'actor')

    def addDirector(self, person):
        """
        adds person to director table given person object
        :param person: person object
        :return: id in director table
        """
        return self._addPerson(person, 'director')

    def _getPersonId(self, person, table):
        """
        gets person id in given table and given person object
        :param person: person object
        :param table: target table
        :return:
        """
        cursor = self.conn.cursor()
        cursor.execute(get_person_id_query % (table, person.first_name, person.last_name))
        try:
            return cursor.fetchall()[0][0]
        except IndexError:
            return None


    def addGenre(self, genre):
        """
        adds new genre to genre table
        :param genre: genre object
        :return: id in genre table
        """
        cursor = self.conn.cursor()
        cursor.execute(add_genre_query % genre.name)
        self.conn.commit()
        return self._getGenreId(genre)

    def _getGenreId(self, genre):
        """
        gets id in genre table for genre object
        :param genre: genre object
        :return: id in genre table
        """
        cursor = self.conn.cursor()
        cursor.execute(get_genre_id_query % genre.name)
        try:
            return cursor.fetchall()[0][0]
        except IndexError:
            return None

    def addFilm(self, film):
        """
        adds film to database including transition tables values
        :param film: Film object
        :return:
        """

        for actor in film.actors:
            actor_id = self._getPersonId(actor, 'actor')
            if actor_id is None:
                actor_id = self.addActor(actor)

        for genre in film.genres:
            genre_id = self._getGenreId(genre)
            if genre_id is None:
                genre_id = self.addGenre(genre)




    def _addFilmRow(self, film):
        """
        add row with title, rel_year, durarion, rating, voters, ranking,
        orig_title
        :param film: object with film
        :return:
        """
        cursor = self.conn.cursor()
        cursor.execute(add_film_row_query % (film.title, film.rel_year, film.duration, film.rating, film.voters, film.ranking))
        self.conn.commit()

    def _addActorInFilmRow(self, film_id, actor_id):
        """
        adds row in actor_in_film table
        :param film_id: film_id
        :param actor_id: actor_id
        :return: None
        """
        cursor = self.conn.cursor()
        cursor.execute(add_actor_in_film_row % (film_id, actor_id))
        self.conn.commit()

    def _addFilmHasGenreRow(self, film_id, genre_id):
        """
        adds row in film_has_genre table
        :param film_id: film_id
        :param genre_id: genre_id
        :return: None
        """
        cursor = self.conn.cursor()
        cursor.execute(add_film_has_genre_row % (film_id, genre_id))
        self.conn.commit()


if __name__ == "__main__":
    imdb_manager = ImdbManager(host, user, password, db)
    # genre = Genre('Action')
    # print(imdb_manager.addGenre(genre))
    # # person = Person(first_name='Jerzy', last_name='Stuhr', nationality='PL')
    # print(imdb_manager.addActor(person))
    # print(imdb_manager.addDirector(person))
    # print(imdb_manager.getActorId(actor))

    # INSERT
    # INTO
    # film(title, relYear, durationMins, rating, voters, ranking)
    # VALUES
    # ('et', '83', '200', '9.9', '200000', '2');

    # et_film = Film(title='et', rel_year='83', duration=200, rating=9.9, ranking=2)
    # imdb_manager._addFilmRow(et_film)

    imdb_manager._addFilmHasGenreRow(3, 2)
    person = Person('Jan', 'P', 'PL')
    print(imdb_manager._getPersonId(person, 'actor'))

