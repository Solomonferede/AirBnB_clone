""" 
The models package
"""


from models.engine import file_storage


storage = file_storage.FileStorage()
print("storage")
storage.reload()