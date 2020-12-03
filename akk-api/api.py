import flask
from flask import jsonify
import sqlite3
import random
import database



app = flask.Flask(__name__)
app.config["DEBUG"] = True




# zwraca listę wszystkich przepisów
@app.route('/products', methods=['GET'])
def products():
    db = database.ConnectToDatabase()
    wynik = database.GetAllProducts(db)
    return jsonify(wynik)





# do zmiany - pobiera z bazy 8 losowych przepisów
@app.route('/recommend', methods=['POST'])
def recommend():
    db = database.ConnectToDatabase()
    RandomNumbersBefore = [1,2,3,4,5,6,7,8,9,10]
    random.shuffle(RandomNumbersBefore)
    RandomNumbers = RandomNumbersBefore[:8]
    RandomNumbers.sort()

    wynik = database.GetSelectedRecipes(RandomNumbers, db)
    for x in range(0,8):
        wynik[x]['skladniki'] = database.GetProductsToRecipes(RandomNumbers[x], db)

    return jsonify(wynik)



app.run()