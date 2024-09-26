# Generated by Django 5.0.6 on 2024-05-24 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0015_alter_qa_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('text', models.TextField()),
                ('img_url', models.CharField(default='', max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]