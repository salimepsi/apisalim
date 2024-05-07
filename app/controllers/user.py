import json


def get_all():
    """function that return all of user in database"""
    try:
        with open("C:\Users\sbouh\OneDrive\Bureau\Pythonpoec\fastapi/app/database/users.json", 'r') as file:
        users = json.load(file)
   
    return users