import flask
from flask import request, jsonify
import requests
import json
import sqlite3





app = flask.Flask(__name__)
app.config["DEBUG"] = True


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d




@app.route('/api', methods=['GET'])
def home():
    db = sqlite3.connect('ZPI.db')
    db.row_factory = dict_factory
    c = db.cursor()
    wynik = c.execute('SELECT Przepisy.Nazwa, Przep_Skład.Id, Składniki.Nazwa FROM Przep_Skład LEFT JOIN Przepisy ON (Przep_Skład.Id_Przepis=Przepisy.Id) INNER JOIN Składniki ON (Przep_Skład.Id_Skład=Składniki.Id)').fetchall()
    # db.close()
    return jsonify(wynik)


@app.route('/api', methods=['POST'])
def wstawianie():
        data = request.get_json()
        db = sqlite3.connect('ZPI.db')
        db.row_factory = dict_factory
        c = db.cursor()
        for x in data:
            c.execute("insert into Składniki values(?,?);", (data[x]['Id'], data[x]['Nazwa'])).fetchall()
        db.commit()

        # c.close()

        # except Exception as E:
        #     return jsonify('Error : ', E)
        # else:
        #     db.commit()
        return jsonify('data inserted')



app.run()