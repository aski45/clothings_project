# Generated by Django 3.1.5 on 2021-01-20 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainapp', '0009_product_false_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catagory',
            name='garment_type',
            field=models.CharField(blank=True, choices=[('Mens', 'Mens'), ('Womens', 'Womens'), ('Kids', 'Kids'), ('Other', 'Other')], max_length=50),
        ),
    ]
