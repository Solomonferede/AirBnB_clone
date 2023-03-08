"""
base_model module

defines all common attributes/methods for other classes:

"""


import datetime
import uuid


class BaseModel:
    """defines all common attributes/methods for other classes:"""

    def __init__(self):
        """Public instance attributes: instantination"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>"""
        return "[" + self.__class__.__name__ + "] (" + str(self.id) + ") " + str(self.__dict__)
    def save(self):
        """Update the public instance attributes updated at"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance:"""
        my_dict = self.__dict__
        for key, value in my_dict.items():
            if key == "updated_at" or key == "created_at":
                value = value.isoformat()
                my_dict[key] = value
        my_dict["__class__"] = self.__class__.__name__
        return my_dict