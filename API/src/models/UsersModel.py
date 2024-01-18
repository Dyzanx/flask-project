from src.database.db import get_connection
from src.models.entities.Users import User
import bcrypt

class UsersModel():
    @classmethod 
    def getUsers(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()
            return users

        except Exception as ex:
            raise Exception(ex)
        

    @classmethod
    def saveUser(self, name, lastname, email, password, username):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            salt = bcrypt.gensalt()
            password = str(password)
            secure_password = bcrypt.hashpw(password.encode('utf-8'), salt)

            cursor.execute("INSERT INTO  users (name, lastname, email, password, username) VALUES('{}', '{}', '{}', '{}', '{}')".format(name, lastname, email, secure_password.decode('utf-8'), username))
            connection.commit()

        except Exception as ex:
            raise Exception(ex)
        

    @classmethod
    def getOne(self, email, password):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT password FROM users WHERE email = '{}'".format(email))
            user_password = cursor.fetchone()

            if user_password is not None and bcrypt.checkpw(password.encode('utf-8'), user_password[0].encode('utf-8')):
                cursor.execute("SELECT * FROM users WHERE email = '{}'".format(email))
                user = cursor.fetchone()
                return user
            else:
                return "Invalid user info"

        except Exception as ex:
            raise Exception(ex)
        
    
    @classmethod
    def updateUser(self, id, name, lastname, email, username):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("UPDATE users SET name='{}', lastname='{}', email='{}', username='{}' WHERE id = {}".format(name, lastname, email, username, id))
            connection.commit()
        except Exception as ex:
            raise Exception(ex)

