# Generated by Django 2.2.12 on 2022-04-15 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fac_app', '0003_auto_20220415_0626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='title',
            field=models.CharField(default='1', max_length=20),
        ),
    ]
