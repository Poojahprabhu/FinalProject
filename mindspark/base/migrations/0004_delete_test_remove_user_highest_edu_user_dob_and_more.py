# Generated by Django 5.0.4 on 2024-04-11 14:20

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_test'),
    ]

    operations = [
        migrations.DeleteModel(
            name='test',
        ),
        migrations.RemoveField(
            model_name='user',
            name='highest_edu',
        ),
        migrations.AddField(
            model_name='user',
            name='dob',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]
