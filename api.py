import requests


def api(tam, level):
    resp = requests.get(
        'http://www.cs.utep.edu/cheon/ws/sudoku/new/?level=' +
        str(level) +
        '&size=' +
        str(tam)
        )

    lista = [["x" for j in range(tam)] for i in range(tam)]

    for item in resp.json()["squares"]:
        lista[item["y"]][item["x"]] = str(item["value"])

    return lista
