# Generated by Django 3.1.7 on 2021-06-29 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_auto_20210630_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='type',
            field=models.CharField(choices=[('menu', 'menu'), ('etkinlik', 'etkinlik'), ('duyuru', 'duyuru'), ('haber', 'haber')], max_length=10),
        ),
    ]
