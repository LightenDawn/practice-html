# Generated by Django 3.2.5 on 2021-08-19 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('responsive_registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='gender',
            field=models.CharField(choices=[('ML', 'ML'), ('FML', 'FML'), ('UNK', 'UNK')], default='UNK', max_length=10),
        ),
    ]
