# Generated by Django 3.1.7 on 2021-06-29 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20210629_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactformmessage',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Closed', 'Closed'), ('Read', 'Read')], default='New', max_length=10),
        ),
        migrations.AlterField(
            model_name='settings',
            name='status',
            field=models.CharField(choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=10),
        ),
    ]
