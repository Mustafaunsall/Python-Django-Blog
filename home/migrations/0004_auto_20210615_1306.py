# Generated by Django 3.1.7 on 2021-06-15 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210615_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='aboutus',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='settings',
            name='contact',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='settings',
            name='references',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='settings',
            name='status',
            field=models.CharField(choices=[('False', 'Hayır'), ('True', 'Evet')], max_length=10),
        ),
    ]
