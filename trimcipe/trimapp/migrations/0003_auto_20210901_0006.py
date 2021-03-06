# Generated by Django 3.2.6 on 2021-09-01 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trimapp', '0002_alter_recipe_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='directions',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='recipeshelf',
            name='recipes',
            field=models.ManyToManyField(blank=True, to='trimapp.Recipe'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='time',
            field=models.IntegerField(),
        ),
    ]
