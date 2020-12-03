import sqlite3
# pip install db-sqlite3
import flask 
# pip install Flask
from flask import request, jsonify


def ConnectToDatabase():
    db = sqlite3.connect('other/ZPI.db')
    db.row_factory = dict_factory
    return db


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d






def GetAllProducts(db):
    with db:
        return db.execute('SELECT Nazwa_Składniki FROM Składniki').fetchall()




def GetSelectedRecipes(RandomNumbers, db):
    with db:
        return db.execute('SELECT Nazwa_Przepisy, Przepis From Przepisy WHERE Id_Przepisy = ? OR Id_Przepisy = ? OR Id_Przepisy = ? OR Id_Przepisy = ? OR Id_Przepisy = ? OR Id_Przepisy = ? OR Id_Przepisy = ? OR Id_Przepisy = ?', [RandomNumbers[0], RandomNumbers[1], RandomNumbers[2], RandomNumbers[3], RandomNumbers[4], RandomNumbers[5], RandomNumbers[6], RandomNumbers[7]]).fetchall()


def GetProductsToRecipes(RandomNumbers, db):
    with db:
        return (db.execute('SELECT Składniki.Nazwa_Składniki, Przep_Skład.Ilość, Przep_Skład.Typ FROM Przep_Skład INNER JOIN Składniki ON (Przep_Skład.Id_Skład=Składniki.Id_Składniki) WHERE Przep_Skład.Id_Przepis = ?', [RandomNumbers]).fetchall())

