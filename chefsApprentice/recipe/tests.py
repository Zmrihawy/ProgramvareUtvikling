from django.test import TestCase
from recipe.models import Ingredient, Recipe
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse
# Create your tests here.

class RecipeTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    # Method to create user
    def create_user(self, username):
        user, created = User.objects.get_or_create(username=username)
        user.set_password('123')
        user.save()
        return user

    # Method to create an ingredient with username = 'usertesting'
    def create_ingredient(self, name):
        user = self.create_user(username='usertesting')
        return Ingredient.objects.create(user=user, name=name)

    # test ingredient model
    def test_ingredient(self):
        ing = self.create_ingredient('testIng1')
        # checks that ing is an instance of Ingredient model
        self.assertTrue(isinstance(ing, Ingredient))
        # checks that ing.name is the same name as in Ingredient_model.name
        self.assertEqual(ing.__str__(), ing.name)
        self.assertEqual(ing.id, 1)

    # Method to create recipe
    def create_recipe(self, username, name='testRec', description='testing recipe', instruction='1. 2.'):
        user = self.create_user(username)
        return Recipe.objects.create(user=user, name=name, description=description, instruction=instruction, view=False)

    # test model recipe
    def test_recipe(self):
        rec1 = self.create_recipe('test1')
        rec2 = self.create_recipe('test2')
        ing1 = self.create_ingredient('testIng1')
        ing2 = self.create_ingredient('testing2')
        # adding 2 ingredients to recipe
        rec1.ingredients.add(ing1)
        rec1.ingredients.add(ing2)
        # checks if recipe is an instance
        self.assertTrue(isinstance(rec1, Recipe))
        # checks if recipe.name is equal to recipe_model.name
        self.assertEqual(rec1.__str__()[0], rec1.name)
        # checks if recipe.view is false
        self.assertFalse(rec1.view)
        # checks that number of ingredients for rec is equal to 2
        self.assertEqual(rec1.ingredients.all().count(), 2)
        # checks that the user creator is the same user in model recipe
        self.assertEqual(rec1.__str__()[1], rec1.user)
        # confirming 2 different users created rec1 and rec2
        self.assertNotEqual(rec2.__str__()[1], rec1.user)

    # test recipe add view
    def test_recipe_add(self):
        #rec = self.create_recipe()
        response = self.client.get('/add_recipe/')
        self.assertEqual(response.status_code, 200)

    # test recipe_detail view
    def test_recipe_view(self):
        response = self.client.get('/recipe/1/')
        self.assertNotEqual(response.status_code, 200)
        rec = self.create_recipe('user1')
        response =self.client.get('/recipe/1/')
        self.assertEqual(response.status_code, 200)
        rec = self.create_recipe('user1')
        response = self.client.get('/recipe/2/')
        self.assertEqual(response.status_code, 200)

    # test recipe_create view
    def test_recipecreate_view(self):
        user = self.create_user('test')
        self.client.login(username='test', password='123')
        rec = self.create_recipe('test')

