import requests


def api(tam):
    resp = requests.get(
        'http://www.cs.utep.edu/cheon/ws/sudoku/new/?level=1&size=' + str(tam)
        )

    lista = [["x" for __ in range(tam)] for _ in range(tam)]

    for item in resp.json()["squares"]:
        lista[item["y"]][item["x"]] = str(item["value"])

    return lista
