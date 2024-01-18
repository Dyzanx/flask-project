class Post():
    def __init__(self, id, user_id, theme_id, title, content, posted_date) -> None:
        self.id = id
        self.user_id = user_id
        self.theme_id = theme_id
        self.title = title
        self.content = content
        self.posted_date = posted_date

    def to_JSON(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "theme_id": self.theme_id,
            "title": self.title,
            "content": self.content,
            "posted_date": self.posted_date,
        }