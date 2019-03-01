import csv
from recipe.models import Recipe
from django.contrib.auth.models import User
CSV_PATH = 'recipes.csv'

count = 0

with open(CSV_PATH, newline='') as csvfile:
    read = csv.reader(csvfile, delimiter=',', quotechar='"')
    print('Loading...')
    for row in read:
        #Recipe.objects.create(user=row[0], name=row[1], description=row[2], instruction=row[3])
        recipe = Recipe()
        recipe.user= User.objects.get(username='admin')
        recipe.name=row[1]
        recipe.description=row[2]
        recipe.instruction=row[3]
        #recipe.image= row[4]
        #recipe.image.save('recipe_image', open(''))
        recipe.save()
        count += 1
    print(f'{str(count)} inserted successfully! ')
