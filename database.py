import mysql.connector
from mysql.connector import Error, connect
from datetime import datetime
import time


class Database:
    def __init__(self, host='localhost', user='andrei', passwd='1234', database='licenta'):
        self._host = host
        self._user = user
        self._passwd = passwd
        self._database = database

    def create_connection(self):
        connection = mysql.connector.connect(
            host=self._host, user=self._user, passwd=self._passwd, database=self._database, connection_timeout=5)
        return connection

    def insert(self, values):
        connection = None
        try:
            connection = self.create_connection()
            cursor = connection.cursor(buffered=True)
            query = """INSERT INTO valori (time, x, y, z) VALUES (%s, %s, %s, %s);"""
            cursor.execute(query, (values.timestamp, values.x, values.y, values.z))
            connection.commit()
            return True if cursor.rowcount > 0 else False
        except mysql.connector.Error as error:
            print('error: ', error)
        finally:
            if (connection is not None):
                cursor.close()
                connection.close()


if __name__ == '__main__':
    db = Database()
