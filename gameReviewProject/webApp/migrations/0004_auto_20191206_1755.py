# Generated by Django 3.0 on 2019-12-06 23:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0003_auto_20191202_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='game_summary',
            field=models.TextField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='reviewers_opinion',
            field=models.TextField(blank=True, default=1),
            preserve_default=False,
        ),
    ]