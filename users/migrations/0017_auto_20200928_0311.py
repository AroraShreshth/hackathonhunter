# Generated by Django 3.1 on 2020-09-27 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20200926_0520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('T', 'Transgender'), ('P', 'Prefer Not To Say'), ('N', 'Non Binary,Gender Queer or gender non-confirming')], max_length=1),
        ),
    ]
