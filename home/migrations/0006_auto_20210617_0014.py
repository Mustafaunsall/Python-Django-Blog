# Generated by Django 3.1.7 on 2021-06-16 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210616_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactformmessage',
            name='status',
            field=models.CharField(choices=[('Read', 'Read'), ('New', 'New')], default='New', max_length=10),
        ),
        migrations.AlterField(
            model_name='settings',
            name='status',
            field=models.CharField(choices=[('False', 'Hayır'), ('True', 'Evet')], max_length=10),
        ),
    ]
