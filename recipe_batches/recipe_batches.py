#!/usr/bin/python

import math
test_recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
test_ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }

def recipe_batches(recipe, ingredients):
  batches = 0
  while True:
    for value in recipe:
      if value not in ingredients:
        return batches
      elif recipe[value] > ingredients[value]:
        return batches
      else:
        ingredients[value] -= recipe[value] 
    batches += 1

recipe_batches(test_recipe, test_ingredients)



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))