# import requests

# import database

# ENDPOINT = "http://localhost:5000"

# def test_db_GetAllProducts():
#     res = database.GetAllProducts()
#     # for el in res: print(el, '\n')
#     assert type(res) != None 


# def test_db_GetAllRecipesNames():
#     res = database.GetAllRecipesNames()
#     # for el in res: print(el, '\n')
#     assert type(res) != None 


# def test_db_GetAllRecipes():
#     res = database.GetAllRecipes()
#     # for el in res: print(el, '\n')
#     assert type(res) != None 


# def test_api_products():
    
#     r = requests.get(ENDPOINT + '/products')
#     print(r.json())


# def test_api_recipes():
#     pass


# if __name__ == "__main__":
    # test_db_GetAllProducts()
    # test_db_GetAllRecipesNames()
    # test_db_GetAllRecipes()

import json
from pprint import pprint

import requests

ENDPOINT = "http://localhost:5000"

r = requests.get(ENDPOINT + '/ping')
print('\n\n\nENDPOINT: /ping')
print(r.status_code)
print(r.content)

r = requests.get(ENDPOINT + '/products')
print('\n\n\nENDPOINT: /products')
print(r.status_code)
pprint(r.json())

r = requests.get(ENDPOINT + '/recipes')
print('\n\n\nENDPOINT: /recipes')
print(r.status_code)
pprint(r.json())


data = json.dumps({'skladnik': 'Chili con carne'})
r = requests.post(ENDPOINT + '/showrecipe', data=data)
print('\n\n\nENDPOINT: /showrecipe')
print('\nSENDING DATA: ' + data)
print(r.status_code)
if r.status_code == 200: pprint(r.json())


data = json.dumps({'skladniki': ['ziemniaki', 'jajka', 'sól', 'mąka']})
# data = json.dumps({'skladniki': ['banan']})
r = requests.post(ENDPOINT + '/recommend', data=data)
print('\n\n\nENDPOINT: /recommend')
print('\nSENDING DATA: ' + data)
print(r.status_code)
if r.status_code == 200: pprint(r.json())