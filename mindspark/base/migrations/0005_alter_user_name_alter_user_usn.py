# Generated by Django 5.0.4 on 2024-04-11 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_delete_test_remove_user_highest_edu_user_dob_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='usn',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
