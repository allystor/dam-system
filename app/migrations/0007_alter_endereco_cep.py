# Generated by Django 4.1.3 on 2023-06-23 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_endereco_cep_alter_engenheiro_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='cep',
            field=models.CharField(max_length=10),
        ),
    ]