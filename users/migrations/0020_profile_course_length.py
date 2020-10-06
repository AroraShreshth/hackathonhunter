# Generated by Django 3.1 on 2020-10-06 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_auto_20201006_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='course_length',
            field=models.CharField(choices=[('3', '3 year'), ('4', '4 year')], default=4, max_length=1),
            preserve_default=False,
        ),
    ]
