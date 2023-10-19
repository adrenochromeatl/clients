# Generated by Django 4.2.6 on 2023-10-19 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rezon', '0003_remove_establishment_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelFiscalRegistrar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите модель ФР', max_length=30, verbose_name='Модель ФР')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ModelFiscalStorage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите модель Фискального Накопителя', max_length=30, verbose_name='Модель Фискального Накопителя')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]