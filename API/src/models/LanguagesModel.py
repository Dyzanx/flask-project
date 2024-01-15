from src.database.db import get_connection
from src.models.entities.Languages import Language

class LanguagesModel:

    @classmethod
    def getLanguages(self):
        try:
            connection = get_connection()
            
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM languages")
            languges  = cursor.fetchall()
            return languges
        
        except Exception as ex:
            raise Exception(ex)
        

    @classmethod
    def getLanguage(self, id):
        try:
            if id:
                cursor = get_connection().cursor()
                cursor.execute("SELECT * FROM languages WHERE id = {}".format(id))
                language = cursor.fetchone()
                return language
            else:
                return {"message": "You must send an ID to being the data search"}
        except Exception as ex:
            raise Exception(ex)
        

    @classmethod
    def saveLanguage(self, name, description):
        try: 
            if name and description:
                connection = get_connection()
                cursor = connection.cursor()
                cursor.execute("INSERT INTO languages (name, description) VALUES('{}', '{}')".format(name, description))
                connection.commit()
            else:
                return {"message": "You must send the NAME and a DESCRIPTION"}
        except Exception as ex:
            print(ex)
            raise Exception(ex)
        

    @classmethod
    def updateLanguage(self, id, name, description):
        try:
            if id and name or id and description:
                connection = get_connection()
                cursor = connection.cursor()
                query = ""

                if name and description:
                    query = "UPDATE languages SET name = '{}', description = '{}' WHERE id = {}".format(name, description, id)
                elif name:
                    query = "UPDATE languages SET name = '{}' WHERE id = {}".format(name, description, id)
                elif description:
                    query = "UPDATE languages SET description = '{}' WHERE id = {}".format(name, description, id)

                cursor.execute(query)
                connection.commit()
                return "updated succesfully"

            else:
                return {"message": "You must send the ID and some data(name or description) to update"}
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def deleteLanguage(self, id):
        try:
            if id:
                connection = get_connection()
                cursor = connection.cursor()
                cursor.execute("DELETE FROM languages WHERE id = {}".format(id))
                connection.commit()
            else:
                return {"message": "You must send an ID to delete the data"}
        except Exception as ex:
            raise Exception(ex)
