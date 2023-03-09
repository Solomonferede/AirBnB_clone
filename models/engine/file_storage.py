#!/usr/bin/python3
"""
The file_storage module
serializes instances to a JSON file and deserializes JSON file to instances:
"""


import json
from os import path
from models.base_model import BaseModel


class FileStorage:
    """serialize and deserialise"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects[obj.__class__.__name__ + '.' + str(obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        print("Solomon")
        my_dict_obj = {}
        for key, value in self.__objects.items():
            my_dict_obj[key] = value.to_dict()
        json_object = json.dumps(my_dict_obj)
        with open(self.__file_path, mode='w+', encoding='utf-8') as fp:
            fp.write(json_object)            

    def reload(self):
        """ deserializes the JSON file to __objects, if path exists or do
        nothing. no exceptions should raise """

        obj_dict = {"BaseModel": BaseModel}
        if path.isfile(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                x = json.loads(f.read())
                for key, value in x.items():
                    self.__objects[key] = obj_dict[value["__class__"]](**value)