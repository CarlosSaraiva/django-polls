# Generated by Django 2.1 on 2018-09-14 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateField(auto_now=True, verbose_name='date published'),
        ),
    ]
