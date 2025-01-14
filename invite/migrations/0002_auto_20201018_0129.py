# Generated by Django 3.1 on 2020-10-17 19:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('invite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invite',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='invite',
            name='usedby_user',
            field=models.ManyToManyField(blank=True, related_name='inviteused', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='invite',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invite', to=settings.AUTH_USER_MODEL),
        ),
    ]
