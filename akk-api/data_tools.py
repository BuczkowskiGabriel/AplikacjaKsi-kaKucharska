def process_data(dane, counting=False):
    """Przerób dane tak, aby składniki
    były pogrupowane wg przepisów"""
    
    wynik = {}

    for el in dane:
        if el['Id_Przepisy'] not in wynik:
            wynik[el['Id_Przepisy']] = {
                'Nazwa_Przepisy': el['Nazwa_Przepisy'],
                'Przepis': el['Przepis'],
                'Składniki': [{
                    'Nazwa_Składniki': el['Nazwa_Składniki'],
                    'Ilość': el['Ilość'],
                    'Typ': el['Typ'],
                }]
            }
        else:
            wynik[el['Id_Przepisy']]['Składniki'].append({
                    'Nazwa_Składniki': el['Nazwa_Składniki'],
                    'Ilość': el['Ilość'],
                    'Typ': el['Typ'],
            })

    return wynik