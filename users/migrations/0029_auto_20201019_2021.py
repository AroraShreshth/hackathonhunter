# Generated by Django 3.1 on 2020-10-19 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0028_auto_20201015_0234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='skill',
            field=models.ManyToManyField(blank=True, related_name='profile', to='users.Skill'),
        ),
    ]
