# Generated by Django 3.1 on 2020-09-25 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20200925_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]
