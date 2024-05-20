# Generated by Django 5.0.4 on 2024-05-20 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('genre', models.CharField(max_length=39)),
                ('characters', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=50)),
            ],
        ),
    ]