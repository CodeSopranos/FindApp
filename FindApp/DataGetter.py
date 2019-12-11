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

    def createDB(self,dbname):
        try:
            self.cursor.execute('create database '+dbname)
        except:
            print('DATABASE '+ dbname + ' already exists')

    def createTables(self):
        try:
            self.cursor.execute('call createTables();')
        except:
            print('CREATING TABLES ERROR')

    def fillTables(self):
        try:
            self.cursor.execute('call fillAllTables();')
        except:
            print('FILL TABLES ERROR')

    def clearTables(self):
        try:
            self.cursor.execute('select clearTables(\'{Child,School,Meeting,Visit}\');')
        except:
            print('CLER TABLES ERROR')

    def insertIntoBase(self, info_dct):
        info_str = '\''+info_dct['name'] + '\''+', ' +'\''+ info_dct['age']+'\'' \
                   + ', ' +'\''+ info_dct['school'] +'\''+ ', ' + '\''+info_dct['meeting']+'\''
        try:
            print(info_str)
            self.cursor.execute('call insertIntoBase('+info_str+');')
        except:
            print('INSERT TABLES ERROR')


    def executeScript(self,script_name):
        # try:
        self.cursor.execute(open('sql/'+script_name, "r").read())
        # except:
        #     print( script_name+' ERROR')

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
