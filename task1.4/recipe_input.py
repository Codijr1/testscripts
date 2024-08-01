#imports
import pickle

#block to calculate difficulty
def calc_difficulty(cooking_time, ingredients):
    if cooking_time < 10:
        if len(ingredients) < 4:
            difficulty = 'Easy'
        else:
            difficulty = 'Intermediate'
    else:
        if len(ingredients) < 4:
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

#instruct user to enter a file name
filename = input("Enter the filename to open: ")

#try-except-else-finally
try:
    file = open(filename, 'rb')
    data = pickle.load(file)
except FileNotFoundError:
    data = {
        'recipes_list':[],
        'all_ingredients':[]
    }
except:
    data = {
        'recipes_list':[],
        'all_ingredients':[]
    }
else:
    file.close()
finally:
    recipes_list = data['recipes_list']
    all_ingredients = data['all_ingredients']

#require number of recipes from user
n = int(input("How many recipes will you be adding? Enter a number: "))

#for loop
for _ in range(n):
    recipe = take_recipe()
    recipes_list.append(recipe)

#adding ingredients to master list
    for ingredient in recipe['ingredients']:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)


#prepare data for uplaod to bin
    data = {
        'recipes_list': recipes_list,
        'all_ingredients': all_ingredients,
    }

#open bin file and add data to it
with open(filename, 'wb') as file:

#writes data to bin file
    pickle.dump(data,file)


#print lists
print(f"Recipes List: {recipes_list}")
print(f"All Ingredients: {all_ingredients}")