import sqlite3
import random
import json

from flask import Flask, request, Response, jsonify
from flask_cors import CORS

import database
from data_tools import process_data
from recommender import make_recommendation

app = Flask(__name__)
app.config["DEBUG"] = True
# Potrzebne by nie było błędów z CORS-em
# (moduł m.in. dodaje OPTIONS i headery)
CORS(app)


@app.route('/ping', methods=['GET'])
def ping():
    return 'Pong'


@app.route('/products', methods=['GET'])
def products():
    """Zwraca listę wszystkich produktow"""

    wynik = database.GetAllProducts()
    wynik = [el.get('Nazwa_Składniki') for el in wynik]

    return jsonify(wynik)


@app.route('/recipes', methods=['GET'])
def recipes():
    """Zwraca listę wszystkich nazw przepisów"""

    wynik = database.GetAllRecipes()
    wynik = list(set([el.get('Nazwa_Przepisy') for el in wynik]))

    return jsonify(wynik)


@app.route('/showrecipe', methods=['POST'])
def show_recipe():
    """Pokaz pojedynczy przepis, ktory ma wybrana nazwe"""
    # Trzeba dodac, by SQLite dobrze przetqworzył zapytanie
    # (bez apostrofow nazwa ze spacjami, bedzie widoczna
    # jak kilka osobnych nazw)
    try:
        if p:=json.loads(request.data).get('skladnik'):
            nazwa_przepisu = '\'' + str(p) + '\''
        else:
            raise AttributeError
        
        dane = database.ShowRecipe(nazwa_przepisu)
        wynik = process_data(dane)

        return jsonify(wynik)
    except AttributeError:
        return Response("\{\}", status=400, mimetype='application/json')
    except:
        return Response("\{\}", status=500, mimetype='application/json')


@app.route('/recommend', methods=['POST'])
def recommend():
    """Podane rekomendacje na podstawie wektora składników"""

    try:
        skladniki = json.loads(request.data).get('skladniki')

        wynik = make_recommendation(skladniki)

        return jsonify(wynik)
    except AttributeError:
        return Response("\{\}", status=400, mimetype='application/json')
    except:
        return Response("\{\}", status=500, mimetype='application/json')


app.run()