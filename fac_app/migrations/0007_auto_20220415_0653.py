# Generated by Django 2.2.12 on 2022-04-15 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fac_app', '0006_faculty_specialization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialization',
            name='special',
            field=models.CharField(default='1', max_length=20),
        ),
    ]
