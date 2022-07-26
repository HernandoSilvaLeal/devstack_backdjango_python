# Generated by Django 4.0.6 on 2022-08-06 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_alter_stagesmodel_number_stage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stagesmodel',
            name='number_stage',
            field=models.IntegerField(choices=[('------', '------'), ('primera', 'Primera'), ('segunda', 'Segunda'), ('tercera', 'Tercera'), ('cuarta', 'Cuarta'), ('quinta', 'Quinta'), ('sexta', 'Sexta'), ('septima', 'Septima'), ('octava', 'Octava'), ('novena', 'Novena'), ('decima', 'Decima'), ('undecima', 'Undecima'), ('duodecima', 'Duodecima')], verbose_name='Cantidad de Etapas'),
        ),
    ]
