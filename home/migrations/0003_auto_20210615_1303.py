# Generated by Django 3.1.7 on 2021-06-15 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210615_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='facebook',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='settings',
            name='instagram',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='settings',
            name='twitter',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]