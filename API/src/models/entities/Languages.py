class Language():

    def __init__(self, id, name=None, description=None) -> None:
        self.id = id
        self.name = name
        self.description = description
        
    
    def to_JSON(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'description' : self.description
        }
