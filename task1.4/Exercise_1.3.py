#task 1.3

#initialize values
recipes_list = []
ingredients_list = []


def take_recipe():
    name = input("Name of dish: ")
    cooking_time = int(input("Cooking time in minutes: "))

#entering ingredients
    ingredients = []
    print("Enter the recipe's ingredients one at a time, and type 'done' when finished: ")

    while True:
        ingredient = input("Enter an ingredient: ")
        if ingredient.lower() == 'done':
            break
        ingredients.append(ingredient)

#creating the dictionary
    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients,
    }

    return recipe

#get the number of recipes to enter
n = int(input("How many recipes would you like to enter? Type a whole number: "))

for i in range(n):
    print(f"\nEntering details for recipe {i + 1}:")
    recipe = take_recipe()
    
    for ingredient in recipe['ingredients']:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)
    
#ppend recipe to master list
    recipes_list.append(recipe)

#printing recipes with difficulty
print("\nRecipes with Difficulty:")
for recipe in recipes_list:
    if recipe['cooking_time'] < 10:
        if len(recipe['ingredients']) < 4:
            difficulty = 'Easy'
        else:
            difficulty = 'Intermediate'
    else:
        if len(recipe['ingredients']) < 4:
            difficulty = 'Intermediate'
        else:
            difficulty = 'Hard'
    
#printing recipe details
    print(f"\nRecipe: {recipe['name']}")
    print(f"Cooking Time (minutes): {recipe['cooking_time']}")
    print("Ingredients:")
    for ingredient in recipe['ingredients']:
        print(f"- {ingredient}")
    print(f"Difficulty level: {difficulty}")

#printing unique ingredients list
print("\nIngredients Available Across All Recipes:")
for ingredient in sorted(ingredients_list):
    print(f"- {ingredient}")
