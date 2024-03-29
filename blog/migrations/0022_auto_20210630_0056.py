# Generated by Django 3.1.7 on 2021-06-29 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20210630_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.CharField(choices=[('False', 'Hayır'), ('True', 'Evet')], max_length=10),
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.CharField(choices=[('False', 'Hayır'), ('True', 'Evet')], max_length=10),
        ),
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('False', 'Hayır'), ('New', 'Yeni'), ('True', 'Evet')], default='New', max_length=10),
        ),
    ]
