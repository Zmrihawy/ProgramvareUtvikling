# Generated by Django 2.1.7 on 2019-03-25 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0007_auto_20190325_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='view',
            field=models.BooleanField(default=False, verbose_name='check this box to make your recipe private'),
            preserve_default=False,
        ),
    ]
