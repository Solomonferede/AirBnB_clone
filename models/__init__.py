#!/usr/bin/python3
""" 
The models package
"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
print("storage")
storage.reload()