# Generated by Django 3.1.7 on 2021-06-30 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_auto_20210630_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('True', 'Evet'), ('New', 'Yeni'), ('False', 'Hayır')], default='New', max_length=10),
        ),
    ]
