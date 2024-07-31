#imports
import pickle

#block to calculate difficulty
def calc_difficulty(cooking_time, ingredients):
    if cooking_time <10:
        if len(ingredients) <4:
            difficulty = 'Easy'
        else:
            difficulty = 'Medium'
    else:
        if len(ingredients) <4:
            difficulty = 'Intermediate'
        else:
            difficulty = 'Hard'
    
    return difficulty


def take_recipe():
    name = input("Name of item: ")
    cooking_time = int(input("Cooking time in minutes: "))

    #recording ingredients from user
    ingredients = []
    print("Enter the recipe's ingredients one at a time, and type 'done' when finished: ")

    while True:
        ingredient = input("Enter an ingredient: ")
        if ingredient.lower() == 'done':
            break
        ingredients.append(ingredient)

    #calculate difficulty
    difficulty = calc_difficulty(cooking_time, ingredients)

    #create the dictionary
    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients,
        'difficulty': difficulty
    }

    return recipe
