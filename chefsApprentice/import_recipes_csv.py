import csv
from recipe.models import Recipe, Ingredient
from django.contrib.auth.models import User
CSV_PATH = 'recipes.csv'

count = 0

with open(CSV_PATH, newline='', encoding='utf-8') as csvfile:
    read = csv.reader(csvfile, delimiter=',', quotechar='"')

    print('Loading...')
    for row in read:
        #Recipe.objects.create(user=row[0], name=row[1], description=row[2], instruction=row[3])
        recipe = Recipe()
        recipe.user= User.objects.get(username=row[0])
        recipe.name=row[1]
        recipe.description=row[2]
        recipe.instruction=row[3]
        #recipe.ingredients= Ingredient.objects.get(Ingredient.set())
        #recipe.image= row[5]
        #recipe.image.save('recipe_image', open(''))
        recipe.save()
        count += 1
        print(f'{str(row[0])} added recipe nr. {str(count)} {str(row[1])}')
    print(f'{str(count)} recipes inserted successfully! ')
