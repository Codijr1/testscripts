import pickle 

#define display_recipe()
def display_recipe(recipe):
    print("Recipe Name:", recipe['name'])
    print("Cooking Time (minutes):", recipe['cooking_time'])
    print("Ingredients:")
    for ingredient in recipe['ingredients']:
        print("-", ingredient)
    print("Difficulty Level:", recipe['difficulty'])

#define search_ingredient()
def search_ingredient(data):
    
    #shows all ingredients
    print("Available Ingredients:")
    for index, ingredient in enumerate(data['all_ingredients']):
        print(f"{index}. {ingredient}")
    
    try:
        #an ingredient is chosen by integer
        choice = int(input("Enter a number for the ingredient you want to search: "))
        ingredient_searched = data['all_ingredients'][choice]
    except (ValueError,IndexError):
        print("Invalid, try entering a valid number.")
        return
    
    #searches for recipes containing selected ingredient
    print(f"Recipes containing  '{ingredient_searched}':")
    for recipe in data['recipes_list']:
        if ingredient_searched in recipe['ingredients']:
            display_recipe(recipe)

#request filename
filename = input("Enter the filename of your recipe")

#load recipe from bin file
try: 
    with open(filename,'rb') as file:
        data = pickle.load(file)
except FileNotFoundError:
    print("Recipe not found")
    data = None
else:
    search_ingredient(data)