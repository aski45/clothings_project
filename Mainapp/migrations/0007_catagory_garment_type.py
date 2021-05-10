# Generated by Django 3.1.5 on 2021-01-19 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainapp', '0006_auto_20210119_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='catagory',
            name='garment_type',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('K', 'Kids'), ('O', 'Other')], max_length=1),
        ),
    ]
