# Generated by Django 5.1.6 on 2025-04-05 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Puzzle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('difficulty_level', models.CharField(max_length=10)),
                ('chess_position', models.CharField(max_length=100)),
                ('solution', models.CharField(max_length=100)),
            ],
        ),
    ]
