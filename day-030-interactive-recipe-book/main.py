import json
def load_recipes(filename='recipes.json'):
    with open(filename, 'r') as file:
        return json.load(file)
def find_recipe(recipes, ingredient):
    return [recipe for recipe in recipes if ingredient in recipe['ingredients']]
def display_recipe(recipe):
    print(f"Recipe: {recipe['name']}")
    print("Ingredients:")
    for ingredient in recipe['ingredients']:
        print(f"- {ingredient}")
    print("Instructions:")
    for step in recipe['instructions']:
        print(f"- {step}")
def main():
    recipes = load_recipes()
    ingredient = input("Enter an ingredient to search for recipes: ")
    results = find_recipe(recipes, ingredient)
    if not results:
        print("No recipes found.")
    else:
        for recipe in results:
            display_recipe(recipe)
if __name__ == '__main__':
    main()
