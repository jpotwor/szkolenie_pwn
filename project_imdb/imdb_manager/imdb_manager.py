import pymysql
from project_imdb.config import host, user, password, db
from project_imdb.imdb_manager.imdb_queries import add_actor_query, get_actor_id_query

class Actor:
    """
    Hods data about actor
    """
    def __init__(self, first_name, last_name, nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.nationality = nationality


class ImdbManager:

    def __init__(self, host, user, password, db):
        """
        class constructor:
        -) connect to DB
        """
        self.conn = pymysql.connect(host=host, user=user, password=password, charset='utf8', db=db)

    def addActor(self, actor):
        """
        adds actor to actor table given first actor object
        :param actor: actor object
        :return: id in actor table
        """
        # create cursor
        cursor = self.conn.cursor()
        cursor.execute(add_actor_query % (actor.first_name, actor.last_name, actor.nationality))
        self.conn.commit()

    def getActorId(self, actor):
        """
        gets actor id actor object
        :param actor: actor object
        :return:
        """
        # create cursor
        cursor = self.conn.cursor()
        cursor.execute(get_actor_id_query %(actor.first_name, actor.last_name))
        return cursor.fetchall()[0][0]


if __name__ == "__main__":
    imdb_manager = ImdbManager(host, user, password, db)
    actor = Actor(first_name='Jerzy', last_name='Stuhr', nationality='PL')
    print(imdb_manager.getActorId(actor))
