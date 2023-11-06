# Generated by Django 4.2.6 on 2023-11-06 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите Имя', max_length=20, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, help_text='Введите фамилию', max_length=20, null=True, verbose_name='Фамилия')),
                ('position', models.CharField(blank=True, help_text='Введите должность', max_length=20, null=True, verbose_name='Должность')),
                ('phone', models.CharField(help_text='Введите номер телефона (с 7 без +)', max_length=11, verbose_name='Номер телефона')),
                ('telega', models.CharField(blank=True, help_text='Введите ссылку/логин в Telegram', max_length=30, null=True, verbose_name='Telegram')),
                ('other', models.CharField(blank=True, help_text='Добавьте заметку', max_length=200, null=True, verbose_name='Примечание')),
            ],
        ),
        migrations.CreateModel(
            name='FiscalRegistrar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zn', models.CharField(help_text='Введите ЗАВОДСКОЙ номер', max_length=30, verbose_name='Заводской номер')),
                ('rn', models.CharField(help_text='Введите РЕГИСТРАЦИОННЫЙ номер', max_length=30, verbose_name='Регистрационный номер')),
                ('reg_card', models.FileField(blank=True, help_text='Прикрепите карточку ККТ', null=True, upload_to='reg_cards', verbose_name='Карточка ККТ')),
            ],
            options={
                'ordering': ['legal'],
            },
        ),
        migrations.CreateModel(
            name='Legal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите наименование юр. лица', max_length=30, verbose_name='Юр. лицо')),
                ('inn', models.CharField(blank=True, help_text='Введите ИНН юр. лица', max_length=10, null=True, verbose_name='ИНН')),
                ('other', models.CharField(blank=True, help_text='Добавьте заметку', max_length=200, null=True, verbose_name='Примечание')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
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
        migrations.CreateModel(
            name='Ofd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите наименование ОФД', max_length=25, verbose_name='Название')),
                ('inn', models.CharField(help_text='Введите ИНН ОФД', max_length=10, verbose_name='ИНН')),
                ('address', models.CharField(help_text='Введите адрес для подключения', max_length=25, verbose_name='Адрес, не IP')),
                ('ip', models.GenericIPAddressField(help_text='Введите IP', verbose_name='IP ОФД')),
                ('port', models.IntegerField(help_text='Введите порт для подключения', verbose_name='Порт')),
                ('dns', models.CharField(help_text='Введите DNS', max_length=20, verbose_name='DNS')),
                ('timeout', models.CharField(blank=True, help_text='Таймаут чтения', max_length=5, null=True, verbose_name='Таймаут чтения')),
                ('timeconn', models.CharField(blank=True, help_text='Таймер соединения с ОФД', max_length=6, null=True, verbose_name='Таймер соединения с ОФД')),
                ('timerfn', models.CharField(blank=True, help_text='Таймер опроса ФН', max_length=6, null=True, verbose_name='Таймер опроса ФН')),
                ('sender', models.EmailField(help_text='Адрес отправки чеков', max_length=254, verbose_name='Адрес отправки чеков')),
                ('adrofd', models.CharField(blank=True, help_text='Адрес сайта ОФД', max_length=25, null=True, verbose_name='Адрес сайта ОФД')),
                ('adrfns', models.CharField(default='www.nalog.gov.ru', help_text='Адрес сайта ФНС', max_length=20, verbose_name='Адрес сайта ФНС')),
                ('adrcheck', models.CharField(blank=True, help_text='Адрес проверки чеков', max_length=50, null=True, verbose_name='Адрес проверки чеков')),
                ('adrffd', models.CharField(help_text='Адрес сервера ФФД 1.2', max_length=30, verbose_name='Адрес сервера ФФД 1.2')),
                ('ipffd', models.GenericIPAddressField(help_text='IP сервера ФФД 1.2', verbose_name='IP сервера ФФД 1.2')),
                ('portffd', models.IntegerField(help_text='Порт ФФД 1.2', verbose_name='Порт ФФД 1.2')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='OptEquip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(help_text='Введите модель оборудования', max_length=20, verbose_name='Модель')),
                ('sn', models.CharField(blank=True, help_text='Введите серийный номер оборудования (необязательно)', max_length=30, null=True, verbose_name='Серийный номер')),
                ('other', models.CharField(blank=True, help_text='Добавьте заметку', max_length=200, null=True, verbose_name='Примечание')),
            ],
        ),
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(help_text='Введите модель принтера', max_length=20, verbose_name='Модель принтера')),
                ('sn', models.CharField(blank=True, help_text='Введите серийный номер принтера (необязательно)', max_length=30, null=True, verbose_name='Серийный номер')),
                ('name', models.CharField(blank=True, help_text='Введите имя в iiko (Например отделение, где размещен принтер', max_length=50, null=True, verbose_name='Имя в iiko')),
                ('other', models.CharField(blank=True, help_text='Добавьте заметку', max_length=200, null=True, verbose_name='Примечание')),
            ],
        ),
        migrations.CreateModel(
            name='RDP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Дайте имя подключению (Например на чей сервер это подключение)', max_length=25, verbose_name='Название')),
                ('ip', models.GenericIPAddressField(help_text='Введите IP', verbose_name='IP')),
                ('port', models.IntegerField(help_text='Введите порт для подключения', verbose_name='Порт')),
                ('login', models.CharField(help_text='Введите логин', max_length=20, verbose_name='Логин')),
                ('password', models.CharField(help_text='Введите пароль', max_length=20, verbose_name='Пароль')),
                ('other', models.CharField(blank=True, help_text='Добавьте заметку', max_length=200, null=True, verbose_name='Примечание')),
            ],
        ),
        migrations.CreateModel(
            name='TypeEq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название типа оборудования', max_length=30, verbose_name='Тип дополнительного оборудования')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите номер версии', max_length=11, verbose_name='Версия iiko')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pcname', models.CharField(blank=True, help_text='Введите имя ПК (необязательно)', max_length=20, null=True, verbose_name='Имя ПК')),
                ('stname', models.CharField(help_text='Введите имя как в iiko', max_length=20, verbose_name='Имя станции в iiko')),
                ('anylogin', models.CharField(help_text='Введите логин Anydesk', max_length=10, verbose_name='Логин Anydesk')),
                ('anypass', models.CharField(help_text='Введите пароль Anydesk', max_length=20, verbose_name='Пароль Anydesk')),
                ('other', models.CharField(blank=True, help_text='Добавьте заметку', max_length=200, null=True, verbose_name='Примечание')),
                ('fr', models.ManyToManyField(help_text='Выберите ФР, если он(они) подключен к этой станции', related_name='+', to='rezon.fiscalregistrar', verbose_name='Фискальный регистратор')),
                ('optequip', models.ManyToManyField(help_text='Выберите доп оборудование, если оно привязано к это станции', related_name='+', to='rezon.optequip', verbose_name='Доп. оборудование')),
                ('printers', models.ManyToManyField(help_text='Выберите принтер или принтеры, если они привязаны к это станции (в iiko)', related_name='+', to='rezon.printer', verbose_name='Принтеры')),
            ],
        ),
        migrations.AddField(
            model_name='optequip',
            name='type_equip',
            field=models.ForeignKey(help_text='Выберите тип оборудования', on_delete=django.db.models.deletion.DO_NOTHING, to='rezon.typeeq', verbose_name='Тип оборудования'),
        ),
        migrations.CreateModel(
            name='FiscalStorage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(help_text='Введите заводской номер ФН', max_length=16, verbose_name='Заводской номер')),
                ('validity', models.DateField(blank=True, help_text='Введите дату окончания ФН', null=True, verbose_name='Срок действия ФН')),
                ('other', models.CharField(blank=True, help_text='Добавьте заметку', max_length=200, null=True, verbose_name='Примечание')),
                ('model', models.ForeignKey(help_text="Введите модель ФН(Например: 'Ин15-3')", on_delete=django.db.models.deletion.DO_NOTHING, to='rezon.modelfiscalstorage', verbose_name='Модель')),
            ],
            options={
                'ordering': ['validity'],
            },
        ),
        migrations.AddField(
            model_name='fiscalregistrar',
            name='fn',
            field=models.ForeignKey(blank=True, help_text='Выберите ФН', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='rezon.fiscalstorage', verbose_name='Фискальный накопитель, установленный в ФР'),
        ),
        migrations.AddField(
            model_name='fiscalregistrar',
            name='legal',
            field=models.ForeignKey(help_text='Выберите юр. лицо', on_delete=django.db.models.deletion.DO_NOTHING, to='rezon.legal', verbose_name='Юр. лицо, на которое зарегистрирован ФР'),
        ),
        migrations.AddField(
            model_name='fiscalregistrar',
            name='model',
            field=models.ForeignKey(help_text='Выберите модель оборудования', on_delete=django.db.models.deletion.DO_NOTHING, to='rezon.modelfiscalregistrar', verbose_name='Модель'),
        ),
        migrations.AddField(
            model_name='fiscalregistrar',
            name='ofd',
            field=models.ForeignKey(blank=True, help_text='Выберите ОФД', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='rezon.ofd', verbose_name='ОФД'),
        ),
        migrations.CreateModel(
            name='Establishment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите наименование заведения', max_length=50, verbose_name='Заведение')),
                ('address', models.CharField(help_text='Введите адрес заведения', max_length=50, verbose_name='Адрес')),
                ('other', models.CharField(blank=True, help_text='Добавьте заметку', max_length=200, null=True, verbose_name='Примечание')),
                ('contact', models.ManyToManyField(help_text='Выберите контактное лицо', to='rezon.contact', verbose_name='Контактное лицо')),
                ('stations', models.ManyToManyField(help_text='Выберите станции, установленные в этом заведении', to='rezon.station', verbose_name='Станции')),
            ],
        ),
        migrations.CreateModel(
            name='Corporation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите наименование организации', max_length=50, verbose_name='Организация')),
                ('iiko_server', models.CharField(help_text='Введите адрес сервера', max_length=50, verbose_name='Сервер iiko')),
                ('port', models.IntegerField(default='443', help_text='Введите порт для подключения', verbose_name='Порт')),
                ('uid', models.CharField(blank=True, help_text='Введите UID (необязательно)', max_length=50, null=True, verbose_name='UID')),
                ('other', models.CharField(blank=True, help_text='Добавьте заметку', max_length=200, null=True, verbose_name='Примечание')),
                ('establishments', models.ManyToManyField(help_text='Выберите заведения, входящие в это предприятие', to='rezon.establishment', verbose_name='Список точек')),
                ('rdp', models.ForeignKey(blank=True, help_text='Выберите RDP если есть', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='rezon.rdp', verbose_name='RDP')),
                ('version', models.ForeignKey(help_text='Выберите версию iiko', on_delete=django.db.models.deletion.DO_NOTHING, to='rezon.version', verbose_name='Версия')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='contact',
            name='corporation',
            field=models.ManyToManyField(help_text='Выберите Заведение (или несколько), с которыми работает контакт', to='rezon.corporation', verbose_name='Заведения'),
        ),
    ]
