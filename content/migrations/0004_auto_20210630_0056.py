# Generated by Django 3.1.7 on 2021-06-29 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20210630_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='status',
            field=models.CharField(choices=[('False', 'Hayır'), ('True', 'Evet')], max_length=10),
        ),
        migrations.AlterField(
            model_name='content',
            name='type',
            field=models.CharField(choices=[('menu', 'menu'), ('haber', 'haber'), ('duyuru', 'duyuru'), ('etkinlik', 'etkinlik')], max_length=10),
        ),
        migrations.AlterField(
            model_name='menu',
            name='status',
            field=models.CharField(choices=[('False', 'Hayır'), ('True', 'Evet')], max_length=10),
        ),
    ]