# Generated by Django 4.0.6 on 2022-08-05 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_projectsmodel_adminproject_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectsmodel',
            name='adminproject',
            field=models.CharField(max_length=50, verbose_name='Admin Responsable'),
        ),
    ]
