# Generated by Django 3.1.5 on 2021-01-24 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainapp', '0011_user_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_detail',
            name='pincode',
            field=models.IntegerField(max_length=10, null=True),
        ),
    ]
