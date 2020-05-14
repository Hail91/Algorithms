#!/usr/bin/python

import math
test_recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }   # Test for PT
test_ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 } # Test for PT

def recipe_batches(recipe, ingredients):
  batches = 0   # Initalize a batches variable to zero
  while True:   # Using a while loop to keep the loop running <--- Should probably refactor this as while True is not very clear.
    for value in recipe:  # Loop over recipe dictionary grabbing values out.
      if value not in ingredients:  # If there is a value in recipes that is not in ingredients, break out of the loop and return batches.
        return batches
      elif recipe[value] > ingredients[value]:  # Otherwise, if the value exists in both dictionaries, but there is not enough in the ingredients dict, then break and return batches.
        return batches
      else:   # Otherwise, that means you have enough of that "Value(ingredient)", so subtract the amount required in recipes from the ingredients dict for that specifc ingredient.
        ingredients[value] -= recipe[value] 
    batches += 1  # Increment batches by 1 once you've completed one full loop through the recipes dict where all conditions are passing.

recipe_batches(test_recipe, test_ingredients)  # Test for PT



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))