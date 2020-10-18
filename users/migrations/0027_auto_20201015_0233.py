# Generated by Django 3.1 on 2020-10-14 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0026_auto_20201013_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='users.profile'),
        ),
        migrations.AlterField(
            model_name='schooleducation',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schooleducation', to='users.profile'),
        ),
        migrations.AlterField(
            model_name='work',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='works', to='users.profile'),
        ),
    ]