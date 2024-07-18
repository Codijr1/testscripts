#recipe_1
recipe_1 = {
    "name" : "Tea",
    "cooking_time" : 5,
    "ingredients" : ["tea leaves","water","sugar"]
    }

#recipe_2
recipe_2 ={
    "name" : "Bowl of Cereal",
    "cooking_time" : 1,
    "ingredients" : ["cereal","milk"]
    }

#recipe_3
recipe_3 ={
    "name" : "College Student's Chicken Breast",
    "cooking_time" : 15,
    "ingredients" : ["chicken breast","butter","salt","pepper"]
    }

#recipe_4
recipe_4 ={
    "name" : "Scrambled Eggs",
    "cooking_time" : 7,
    "ingredients" : ["eggs","butter","cheese","salt","pepper"]
    }

#recipe_5
recipe_5 ={
    "name" : "Yogurt Snack",
    "cooking_time" : 2,
    "ingredients" : ["Greek yogurt","oats","mixed fruit"]
    }


#outer structure
all_recipes = [recipe_1,recipe_2,recipe_3,recipe_4,recipe_5]

#code to print each recipe's ingredients as five different lists
print(f"Ingredients for {recipe_1['name']}: {recipe_1['ingredients']}")
print(f"Ingredients for {recipe_2['name']}: {recipe_2['ingredients']}")
print(f"Ingredients for {recipe_3['name']}: {recipe_3['ingredients']}")
print(f"Ingredients for {recipe_4['name']}: {recipe_4['ingredients']}")
print(f"Ingredients for {recipe_5['name']}: {recipe_5['ingredients']}")