# Generated by Django 3.2.5 on 2021-08-13 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('email_address', models.EmailField(max_length=254)),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
