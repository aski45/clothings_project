# Generated by Django 3.1.5 on 2021-01-19 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainapp', '0008_auto_20210119_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='false_price',
            field=models.IntegerField(null=True),
        ),
    ]
