import sys
import psycopg2

class DataGetter:

    """

    @DataGetter class for interaction with databases

    """
    def __init__(self,dbname='nn'):
        self.conn = psycopg2.connect(dbname=dbname, user='postgres', password='36512', host='localhost')
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()


    def executeQuery(self,query):
        self.cursor.execute(query)
        frame = self.cursor.fetchall()
        features=[feature[0] for feature in self.cursor.description]
        return frame, features

    def findRebelQuery(self,name):
        self.cursor.execute('call findRebel(\'%'+name+'%\')')
        frame = self.cursor.fetchall()
        features=[feature[0] for feature in self.cursor.description]
        return frame, features

    def getRebelDataByID(self,id):
        self.cursor.execute('call getrebeldatabyid(\''+id+'\')')
        frame = self.cursor.fetchall()
        features=[feature[0] for feature in self.cursor.description]
        return frame, features
