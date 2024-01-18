class Themes():
    def __init__(self, id, name, date) -> None:
        self.id = id
        self.name = name
        self.date = date

    def to_JSON(self):
        return {
            "id": self.id,
            "name": self.name,
            "date": self.date
        }