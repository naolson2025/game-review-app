# Generated by Django 2.2.7 on 2019-11-29 02:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_summary', models.TextField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('rating', models.IntegerField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='user_images/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]