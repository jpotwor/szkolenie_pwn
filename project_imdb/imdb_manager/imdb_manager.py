import pymysql


class ImdbManager(object):

    def __init__(self, host, user, password):
        """
        class constructor:
        -) connect to DB
        """
        conn = pymysql.connect(host=host, user=user, password=password, charset='utf8')


if __name__ == "__main__":
    imdb_manager = ImdbManager(host='localhost', user='jan', password='jan_pass')
