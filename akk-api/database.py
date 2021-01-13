import sqlite3
import sys
import os

# trzeba dodać by widział baze danych w innej lokacji
root_dir = os.path.dirname(os.path.curdir)
sys.path.append(root_dir)

db = sqlite3.connect('../akk-db/ZPI.db', check_same_thread=False)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def GetAllProducts():
    with db:
        return db.execute('SELECT Nazwa_Składniki FROM Składniki')


def GetAllRecipesNames():
    with db:
        return db.execute('SELECT Nazwa_Przepisy FROM Przepisy')
        

def ShowRecipe(nazwa_przepisu):
    with db:
        return db.execute(f"""
        SELECT p.Id_Przepisy, p.Nazwa_Przepisy, p.Przepis, s.Nazwa_Składniki, ps.Ilość, ps.Typ 
        FROM Składniki s
        INNER JOIN Przep_Skład ps ON s.Id_Składniki=ps.Id_Skład
        INNER JOIN Przepisy p ON ps.Id_Przepis=p.Id_Przepisy
        WHERE p.Nazwa_Przepisy={nazwa_przepisu}
        ORDER BY p.Id_Przepisy ASC
        """)


def GetAllRecipes():
    with db:
        return db.execute("""
        SELECT p.Id_Przepisy, p.Nazwa_Przepisy, p.Przepis, s.Nazwa_Składniki, ps.Ilość, ps.Typ 
        FROM Składniki s
        INNER JOIN Przep_Skład ps ON s.Id_Składniki=ps.Id_Skład
        INNER JOIN Przepisy p ON ps.Id_Przepis=p.Id_Przepisy
        ORDER BY p.Id_Przepisy ASC
        """)


db.row_factory = dict_factory