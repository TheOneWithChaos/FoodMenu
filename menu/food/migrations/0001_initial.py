# Generated by Django 5.0.3 on 2024-05-15 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('image', models.ImageField(default='menu/images/default.jpg', upload_to='menu/images')),
            ],
        ),
    ]
