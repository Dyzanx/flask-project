class User():
    def __init__(self, id, name, lastname, email, password, username) -> None:
        self.id = id
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password
        self.username = username

    def to_JSON(self):
        return {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
            "email": self.email,
            "password": self.password,
            "username": self.username,
        }