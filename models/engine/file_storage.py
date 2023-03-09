#!/usr/bin/python3
"""
The file_storage module
serializes instances to a JSON file and deserializes JSON file to instances:
"""


import json
from os import path


class FileStorage:
    """serialize and deserialise"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        print("newww")
        self.__objects[obj.__class__.__name__ + '.' + str(obj.id)] = self.__dict__

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        print("Solomon")
        with open(self.__file_path, mode='w+', encoding='utf-8') as fp:
            fp.write(json.dumps(self.__objects))

    def reload(self):
        """deserializes the JSON file to __objects"""
        if path.isfile(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as fp:
                __objects = json.load(fp)