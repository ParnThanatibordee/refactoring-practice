from recipe import Recipe

if __name__ == '__main__':
    recipe_list = [["Coffee with sugar", 4, 0, 0, 2, 30.0],
                   ["Latte", 3, 0, 1, 2, 40.0],
                   ["Hot Chocolate", 0, 3, 4, 2, 30.0],
                   ]

    for i in range(len(recipe_list)):
        recipe = Recipe(recipe_list[i][0])
        recipe.coffee = recipe_list[i][1]
        recipe.chocolate = recipe_list[i][2]
        recipe.milk = recipe_list[i][3]
        recipe.sugar = recipe_list[i][4]
        recipe.price = recipe_list[i][5]
        print(recipe)
