# Generated by Django 2.2.6 on 2019-10-06 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='realtor',
            old_name='hired_date',
            new_name='hire_date',
        ),
    ]
