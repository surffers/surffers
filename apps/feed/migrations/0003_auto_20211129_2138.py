# Generated by Django 3.1.3 on 2021-11-29 10:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_auto_20211129_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(default=uuid.uuid4, unique=True),
        ),
    ]