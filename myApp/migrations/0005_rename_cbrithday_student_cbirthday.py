# Generated by Django 4.0.5 on 2022-06-17 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_student_cbrithday'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='cBrithday',
            new_name='cBirthday',
        ),
    ]
