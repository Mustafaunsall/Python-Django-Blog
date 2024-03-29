# Generated by Django 3.1.7 on 2021-06-19 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20210618_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('False', 'Hayır'), ('New', 'Yeni'), ('True', 'Evet')], default='New', max_length=10),
        ),
    ]
