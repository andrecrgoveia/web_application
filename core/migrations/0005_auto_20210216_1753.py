# Generated by Django 3.1.6 on 2021-02-16 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210216_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricing',
            name='description',
            field=models.TextField(max_length=500, verbose_name='Description'),
        ),
    ]
