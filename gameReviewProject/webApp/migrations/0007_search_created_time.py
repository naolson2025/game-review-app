# Generated by Django 3.0 on 2019-12-08 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0006_search'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='created_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
