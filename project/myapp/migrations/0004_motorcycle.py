# Generated by Django 4.2.3 on 2023-07-26 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_public_article_published'),
    ]

    operations = [
        migrations.CreateModel(
            name='Motorcycle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('reference', models.CharField(max_length=80)),
            ],
        ),
    ]
