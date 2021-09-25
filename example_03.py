import pytest


def cakes(recipe, available):

    lista = []

    for key, value in available.items():
        if key in recipe:
            lista.append(value // recipe[key])
    
    for key, value in recipe.items():
        if key not in available:
            return 0
    
    return min(lista)
    

def test_case():
    recipe = {"flour": 500, "sugar": 200, "eggs": 1}
    available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
    assert cakes(recipe, available) == 2

    recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
    available = {"sugar": 500, "flour": 2000, "milk": 2000}
    assert cakes(recipe, available) == 0