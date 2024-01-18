from src.database.db import get_connection
from src.models.entities.Posts import Post

class PostsModel():
    @classmethod
    def getAll(self):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM posts")
            posts = cursor.fetchall()
            return posts

        except Exception as ex:
            raise Exception(ex)
        
    
    @classmethod
    def getOne(self, id):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM posts WHERE id = {}".format(id))
            post = cursor.fetchone()

            return post

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def savePost(self, user_id, theme_id, title, content):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("INSERT INTO posts (user_id, theme_id, title, content, posted_date) VALUES({}, {}, '{}', '{}', CURRENT_DATE)".format(user_id, theme_id, title, content))
            connection.commit()
            
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def updatePost(self, id, title, content):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("UPDATE posts SET title='{}', content='{}' WHERE id = {}".format(title, content, id))
            connection.commit()
            
        except Exception as ex:
            raise Exception(ex)
        
    
    @classmethod
    def deletePost(self, id):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("DELETE FROM posts WHERE id = {}".format(id))
            connection.commit()
            
        except Exception as ex:
            raise Exception(ex)