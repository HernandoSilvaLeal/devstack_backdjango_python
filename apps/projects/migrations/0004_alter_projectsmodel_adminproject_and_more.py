# Generated by Django 4.0.6 on 2022-08-05 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_areasmodel_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectsmodel',
            name='adminproject',
            field=models.CharField(max_length=50, verbose_name='Administrador Responsable'),
        ),
        migrations.AlterField(
            model_name='projectsmodel',
            name='auditorproject',
            field=models.CharField(max_length=50, verbose_name='Auditor Responsable'),
        ),
        migrations.AlterField(
            model_name='projectsmodel',
            name='leaderproject',
            field=models.CharField(max_length=50, verbose_name='Lider Responsable'),
        ),
    ]