import psycopg2
from services.queryService import *


class ConnectionService():
    def __init__(self):
        pass


    def connect():
        return psycopg2.connect(
            database="johnpark",
            user="johnpark",
            password="")

    def close(self):
        self.conn.close()
        print('Database connection closed.')