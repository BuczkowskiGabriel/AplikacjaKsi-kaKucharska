from collections import OrderedDict

import numpy as np

import database
from data_tools import process_data

MAX_RECOMMEDATION = 5


def create_vector_from_products(lista_skladnikow):
    """Utworz wektor potrzebny do liczenia prawdopodobieństwa"""

    wszystkie_skladniki = database.GetAllProducts()
    wszystkie_skladniki = [el.get('Nazwa_Składniki') for el in wszystkie_skladniki]

    ilosc = len(wszystkie_skladniki)
    v = np.zeros(ilosc)
    for id, skladnik in enumerate(wszystkie_skladniki):
        if skladnik in lista_skladnikow: v[id] = 1
    
    return v


def create_vector_from_recipes(przepis):
    """Utworz wektor dla pojedynczego przepisu
    (potrzebne w petli)"""

    lista_skladnikow = [el['Nazwa_Składniki'] for el in przepis['Składniki']]

    return create_vector_from_products(lista_skladnikow)


def probability(v1, v2):
    """Prawdopodobieństwo warunkowe
    - Ile spośród potrzebnych produktów już mamy w lodówce"""

    return round(sum(np.logical_and(v1, v2)) / sum(v2) * 100, 2)


def count_recommendation(lista_skladnikow, wszystkie_przepisy):
    """Dla listy składników i przepisów policz prawdopodobieństwa
    i podaj najlepsze przepisy"""

    v = create_vector_from_products(lista_skladnikow)

    odleglosci = []
    for id_przepisu, przepis in wszystkie_przepisy.items():
        p = create_vector_from_recipes(przepis)
        odleglosci.append((id_przepisu, probability(v, p)))
    
    # porządkuj od najlepszego
    odleglosci.sort(key=lambda x: -x[1])

    return odleglosci[:MAX_RECOMMEDATION]


def make_recommendation(lista_skladnikow):
    """Dla wybranej listy składników podaj najbardziej
    rekomendowane przepisy"""

    dane = database.GetAllRecipes()
    wszystkie_przepisy = process_data(dane, counting=True)

    najlepsze_przepisy = count_recommendation(lista_skladnikow, wszystkie_przepisy)

    # trzeba zapamietac kolejnosc, czego nie robi normalnie dict
    rekomendacja = OrderedDict()
    for id_przepisu, prawdopodobienstwo in najlepsze_przepisy:
        rekomendacja[id_przepisu] = wszystkie_przepisy[id_przepisu]
        # dodatkowe pole do wyswietlania na frontendzie
        rekomendacja[id_przepisu]['prawdopodobienstwo'] = prawdopodobienstwo

    return rekomendacja