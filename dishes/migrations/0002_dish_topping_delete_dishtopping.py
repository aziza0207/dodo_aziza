# Generated by Django 4.0.3 on 2022-04-04 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='topping',
            field=models.ManyToManyField(to='dishes.topping'),
        ),
        migrations.DeleteModel(
            name='DishTopping',
        ),
    ]