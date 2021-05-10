# Generated by Django 3.1.5 on 2021-01-18 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('price', models.IntegerField()),
                ('cod', models.BooleanField()),
                ('emi', models.TextField(max_length=100)),
                ('offer', models.TextField(blank=True)),
                ('return_policy', models.TextField(max_length=50)),
                ('discription', models.TextField(max_length=500)),
                ('image_1', models.ImageField(default='default.jpg', upload_to='products')),
                ('image_2', models.ImageField(default='default.jpg', upload_to='products')),
                ('image_3', models.ImageField(default='default.jpg', upload_to='products')),
            ],
        ),
    ]
