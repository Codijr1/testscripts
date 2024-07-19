# task 1.3
recipes_list = []
ingredients_list = []

def take_recipe():
    name = input("Name of dish: ")
    cooking_time = int(input("Cooking time in minutes: "))

    #entering ingredients
    ingredients = []
    print("Enter the recipe's ingredients one at a time, and enter 'done' when finished: ")

    while True:
        ingredient = input("Enter an ingredient: ")
        if ingredient.lower() == 'done':
            break
        ingredients.append(ingredient)


    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients,
    }

    return recipe

n = int(input("How many recipes would you like to enter? Type a whole number: "))
for i in range(n):
    print(f"\nEntering details for recipe {i + 1}:")
    recipe = take_recipe()
    recipes_list.append(recipe)

#printing results

print("\nRecipes:")
for recipe in recipes_list:
    print(f"\nRecipe: {recipe['name']}")
    print(f"Cooking time: {recipe['cooking_time']} minutes")
    print("Ingredients:")
    for ingredient in recipe['ingredients']:
        print(f"- {ingredient}")