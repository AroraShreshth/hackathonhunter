# Generated by Django 3.1 on 2020-11-22 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comp', '0007_auto_20201123_0039'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='City',
            new_name='city',
        ),
        migrations.AddField(
            model_name='event',
            name='application_review',
            field=models.BooleanField(default=False),
        ),
    ]