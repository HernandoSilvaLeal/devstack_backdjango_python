# Generated by Django 4.0.6 on 2022-08-05 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0003_alter_controlsadmin_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activitiesmodel',
            old_name='name_activity',
            new_name='name',
        ),
    ]
