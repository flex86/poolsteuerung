import sqlite3
class Db(object):
    def __init__(self,config):
        self.connection=config.database
    def insert(self,table,values):
        id=0
        return id

    def update(self,id,table,values):
        return True

    def delete(self,table,id):
        return True

    def fetchOne(self,table):
        return ''
    def fetchAll(self,table):
        return []
    def fetchColumn(self,table,column):
        return []
    def query(self):
        return[]
