# Generated by Django 5.1.1 on 2024-09-09 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome_tarefa', models.CharField(max_length=200)),
            ],
        ),
    ]