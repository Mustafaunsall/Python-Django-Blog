# Generated by Django 3.1.7 on 2021-07-01 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_auto_20210701_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.CharField(choices=[('True', 'Evet'), ('False', 'Hayır'), ('New', 'Yeni')], max_length=10),
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