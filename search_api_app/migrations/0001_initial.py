# Generated by Django 3.2.5 on 2024-02-06 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=255)),
                ('creator', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('number', models.IntegerField()),
                ('dispo', models.BooleanField()),
                ('price', models.FloatField()),
            ],
        ),
    ]