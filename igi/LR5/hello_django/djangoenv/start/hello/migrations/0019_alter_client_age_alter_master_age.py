# Generated by Django 5.0.6 on 2024-06-03 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0018_clientcredentials_mastercredentials'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='age',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='master',
            name='age',
            field=models.DateField(),
        ),
    ]
