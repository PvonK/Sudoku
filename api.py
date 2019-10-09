import requests


def api(tam):
    resp = requests.get('http://www.cs.utep.edu/cheon/ws/sudoku/new/?level=1&size=' + str(tam))
    if tam == 9:
        lista = [["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x", "x", "x", "x", "x"]]
    elif tam == 4:
        lista = [["x", "x", "x", "x"],
                 ["x", "x", "x", "x"],
                 ["x", "x", "x", "x"],
                 ["x", "x", "x", "x"]]
    for item in resp.json()["squares"]:
        lista[item["y"]][item["x"]] = str(item["value"])

    return lista
