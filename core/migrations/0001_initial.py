# Generated by Django 4.1.7 on 2023-02-28 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=100)),
                ('Idade', models.CharField(max_length=3)),
                ('Telefone', models.CharField(max_length=16)),
            ],
        ),
    ]
