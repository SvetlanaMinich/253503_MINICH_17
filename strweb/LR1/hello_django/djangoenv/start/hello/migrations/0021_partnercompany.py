# Generated by Django 5.0.6 on 2024-09-20 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hello", "0020_review_rating"),
    ]

    operations = [
        migrations.CreateModel(
            name="PartnerCompany",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("logo_url", models.CharField(default="", max_length=500)),
                ("website", models.URLField()),
            ],
        ),
    ]