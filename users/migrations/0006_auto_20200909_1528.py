# Generated by Django 3.1 on 2020-09-09 15:28

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200909_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldofstudy',
            name='id',
            field=models.UUIDField(default=uuid.UUID('8e25febf-b85b-473f-b5c5-105b5740084f'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='institute',
            name='id',
            field=models.UUIDField(default=uuid.UUID('8e25febf-b85b-473f-b5c5-105b5740084f'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='link',
            name='id',
            field=models.UUIDField(default=uuid.UUID('8e25febf-b85b-473f-b5c5-105b5740084f'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='field_of_study',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='users.fieldofstudy'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'MALE'), ('F', 'FEMALE'), ('T', 'Transgender'), ('P', 'Prefer Not To Say'), ('N', 'Non Binary,Gender Queer or gender non-confirming')], max_length=1),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.UUIDField(default=uuid.UUID('8e25febf-b85b-473f-b5c5-105b5740084f'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='institute',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='users.institute'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='shirt_size',
            field=models.CharField(blank=True, choices=[('XS', 'Extra Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'X Large'), ('XXL', 'XX Large'), ('XXXL', 'XXX Large')], max_length=4),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skill',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='users.skill'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='id',
            field=models.UUIDField(default=uuid.UUID('8e25febf-b85b-473f-b5c5-105b5740084f'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='work',
            name='id',
            field=models.UUIDField(default=uuid.UUID('8e25febf-b85b-473f-b5c5-105b5740084f'), editable=False, primary_key=True, serialize=False),
        ),
    ]
