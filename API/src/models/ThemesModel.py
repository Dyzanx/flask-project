from src.database.db import get_connection
from src.models.entities.Themes import Themes

class ThemesModel():
    @classmethod
    def getAll(self):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM themes")
            themes = cursor.fetchall()
            return themes
        
        except Exception as ex:
            raise Exception(ex)


    @classmethod 
    def insert(self, name):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("INSERT INTO themes (name, date) VALUES('{}', CURRENT_DATE)".format(name))
            connection.commit()

        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def getOne(self, id):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM themes WHERE id = {}".format(id))
            theme = cursor.fetchone()

            return theme
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def updateTheme(self, id, name):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("UPDATE themes SET name = '{}' WHERE id = {}".format(name, id))
            connection.commit()

        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def deleteTheme(self, id):
        try: 
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("DELETE FROM themes WHERE id = {}".format(id))
            connection.commit()
        except Exception as ex:
            raise Exception(ex)