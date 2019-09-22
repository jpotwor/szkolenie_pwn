import pymysql
from project_imdb.config import host, user, password, db
from project_imdb.imdb_manager.imdb_queries import add_person_query, get_person_id_query, add_genre_query, \
    get_genre_id_query
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
        return cursor.fetchall()[0][0]

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
        return cursor.fetchall()[0][0]

    def addFilm(self, film):
        # check if film exists in table
        # if not add row
        pass

    def _addFilmRow(self, film):
        pass

    def _addActorInFilm(self):
        pass

    def _addGenreInFilm(self):
        pass




if __name__ == "__main__":
    imdb_manager = ImdbManager(host, user, password, db)
    genre = Genre('Action')
    print(imdb_manager.addGenre(genre))
    # person = Person(first_name='Jerzy', last_name='Stuhr', nationality='PL')
    # print(imdb_manager.addActor(person))
    # print(imdb_manager.addDirector(person))
    # print(imdb_manager.getActorId(actor))

