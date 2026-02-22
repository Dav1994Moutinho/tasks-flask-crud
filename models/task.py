class Task:
    def __init__(self, id, title, description, completed=False):
        """ Constructor class """
        self.id = id
        self.title = title
        self.description = description
        self.completed =  completed

    def to_dictionary(self):
        """ Trasform to dictionary """
        return {"id": self.id, 
                "title": self.title, 
                "description": self.description, 
                "completed": self.completed
                }