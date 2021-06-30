# Generated by Django 3.1.7 on 2021-06-30 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_auto_20210630_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.CharField(choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=10),
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.CharField(choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=10),
        ),
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('True', 'Evet'), ('False', 'Hayır'), ('New', 'Yeni')], default='New', max_length=10),
        ),
    ]
