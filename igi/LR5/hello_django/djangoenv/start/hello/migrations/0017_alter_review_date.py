# Generated by Django 5.0.6 on 2024-05-24 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0016_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
