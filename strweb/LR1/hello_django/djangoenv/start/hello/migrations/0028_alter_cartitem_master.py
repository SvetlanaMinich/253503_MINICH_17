# Generated by Django 5.0.6 on 2024-09-21 17:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hello", "0027_alter_cartitem_master"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cartitem",
            name="master",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="hello.master",
            ),
        ),
    ]