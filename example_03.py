# Pete likes to bake some cakes. He has some recipes and ingredients. 
# Unfortunately he is not good in maths. 
# Can you help him to find out, how many cakes he could bake considering his recipes?

# Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns the maximum number of cakes Pete can bake (integer). 
# For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). 
# Ingredients that are not present in the objects, can be considered as 0.


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