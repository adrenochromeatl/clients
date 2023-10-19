from django.db import models
from django.urls import reverse


class TypeEq(models.Model):
    name = models.CharField(max_length=30,
                            help_text="Введите название типа оборудования",
                            verbose_name="Тип дополнительного оборудования")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Version(models.Model):
    name = models.CharField(max_length=11,
                            help_text="Введите номер версии",
                            verbose_name="Версия iiko")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Legal(models.Model):
    name = models.CharField(max_length=30,
                            help_text="Введите наименование юр. лица",
                            verbose_name="Юр. лицо")
    inn = models.CharField(max_length=10,
                           help_text="Введите ИНН юр. лица",
                           verbose_name="ИНН",
                           null=True, blank=True)
    other = models.CharField(max_length=200,
                             help_text="Добавьте заметку",
                             verbose_name="Примечание",
                             null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class FiscalStorage(models.Model):
    number = models.CharField(max_length=16,
                              help_text="Введите заводской номер ФН",
                              verbose_name="Заводской номер",
                              primary_key=True)
    validity = models.DateField(help_text="Введите дату окончания ФН",
                                verbose_name="Срок действия ФН",
                                null=True, blank=True)
    model = models.ForeignKey('ModelFiscalStorage', on_delete=models.DO_NOTHING,
                              help_text="Введите модель ФН(Например: 'Ин15-3'",
                              verbose_name="Модель")
    other = models.CharField(max_length=200,
                             help_text="Добавьте заметку",
                             verbose_name="Примечание",
                             null=True, blank=True)

    def __str__(self):
        return '%s, %s' % (self.number, self.validity)

    def get_absolute_url(self):
        return reverse('fiscal-storage-detail', args=[str(self.number)])

    class Meta:
        ordering = ["validity"]


class Ofd(models.Model):
    name = models.CharField(max_length=25,
                            help_text="Введите наименование ОФД",
                            verbose_name="Название")
    inn = models.CharField(max_length=10,
                           help_text="Введите ИНН ОФД",
                           verbose_name="ИНН")
    address = models.CharField(max_length=25,
                               help_text="Введите адрес для подключения",
                               verbose_name="Адрес, не IP")
    ip = models.GenericIPAddressField(help_text="Введите IP",
                                      verbose_name="IP ОФД")
    port = models.IntegerField(help_text="Введите порт для подключения",
                               verbose_name="Порт")
    dns = models.CharField(max_length=20,
                           help_text="Введите DNS",
                           verbose_name="DNS")
    timeout = models.CharField(max_length=3,
                               help_text="Таймаут чтения",
                               verbose_name="Таймаут чтения",
                               null=True, blank=True)
    timeconn = models.CharField(max_length=6,
                                help_text="Таймер соединения с ОФД",
                                verbose_name="Таймер соединения с ОФД",
                                null=True, blank=True)
    timerfn = models.CharField(max_length=6,
                               help_text="Таймер опроса ФН",
                               verbose_name="Таймер опроса ФН",
                               null=True, blank=True)
    sender = models.EmailField(help_text="Адрес отправки чеков",
                               verbose_name="Адрес отправки чеков")
    adrofd = models.CharField(max_length=25,
                              help_text="Адрес сайта ОФД",
                              verbose_name="Адрес сайта ОФД",
                              null=True, blank=True)
    adrfns = models.CharField(max_length=20,
                              help_text="Адрес сайта ФНС",
                              verbose_name="Адрес сайта ФНС",
                              default="www.nalog.gov.ru")
    adrcheck = models.CharField(max_length=50,
                                help_text="Адрес проверки чеков",
                                verbose_name="Адрес проверки чеков",
                                null=True, blank=True)
    adrffd = models.CharField(max_length=30,
                              help_text="Адрес сервера ФФД 1.2",
                              verbose_name="Адрес сервера ФФД 1.2")
    ipffd = models.GenericIPAddressField(help_text="IP сервера ФФД 1.2",
                                         verbose_name="IP сервера ФФД 1.2")
    portffd = models.IntegerField(help_text="Порт ФФД 1.2",
                                  verbose_name="Порт ФФД 1.2")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ofd-detail', args=[str(self.id)])

    class Meta:
        ordering = ["name"]


class RDP(models.Model):
    name = models.CharField(max_length=25,
                            help_text="Дайте имя подключению (Например на чей сервер это подключение)",
                            verbose_name="Название")
    ip = models.GenericIPAddressField(help_text="Введите IP",
                                      verbose_name="IP")
    port = models.IntegerField(help_text="Введите порт для подключения",
                               verbose_name="Порт")
    login = models.CharField(max_length=20,
                             help_text="Введите логин",
                             verbose_name="Логин")
    password = models.CharField(max_length=20,
                                help_text="Введите пароль",
                                verbose_name="Пароль")
    other = models.CharField(max_length=200,
                             help_text="Добавьте заметку",
                             verbose_name="Примечание",
                             null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('rdp-detail', args=[str(self.id)])


class Printers(models.Model):
    model = models.CharField(max_length=20,
                             help_text="Введите модель принтера",
                             verbose_name="Модель принтера")
    sn = models.CharField(max_length=30,
                          help_text="Введите серийный номер принтера (необязательно)",
                          verbose_name="Серийный номер",
                          null=True, blank=True)
    name = models.CharField(max_length=20,
                            help_text="Введите имя в iiko (Например отделение, где размещен принтер",
                            verbose_name="Имя в iiko",
                            null=True, blank=True)
    other = models.CharField(max_length=200,
                             help_text="Добавьте заметку",
                             verbose_name="Примечание",
                             null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('printer-detail', args=[str(self.id)])


class OptEquip(models.Model):
    model = models.CharField(max_length=20,
                             help_text="Введите модель оборудования",
                             verbose_name="Модель")
    type_equip = models.ForeignKey('TypeEq',
                                   on_delete=models.DO_NOTHING,
                                   help_text="Выберите тип оборудования",
                                   verbose_name="Тип оборудования")
    sn = models.CharField(max_length=30,
                          help_text="Введите серийный номер оборудования (необязательно)",
                          verbose_name="Серийный номер",
                          null=True, blank=True)
    other = models.CharField(max_length=200,
                             help_text="Добавьте заметку",
                             verbose_name="Примечание",
                             null=True, blank=True)

    def __str__(self):
        return '%s, %s' % (self.type_equip, self.model)

    def get_absolute_url(self):
        return reverse('opt-equip-detail', args=[str(self.id)])


class FiscalRegistrar(models.Model):
    model = models.ForeignKey('ModelFiscalRegistrar', on_delete=models.DO_NOTHING,
                              help_text="Выберите модель оборудования",
                              verbose_name="Модель")
    zn = models.CharField(max_length=30,
                          help_text="Введите ЗАВОДСКОЙ номер",
                          verbose_name="Заводской номер",
                          primary_key=True)
    rn = models.CharField(max_length=30,
                          help_text="Введите РЕГИСТРАЦИОННЫЙ номер",
                          verbose_name="Регистрационный номер")
    reg_card = models.FileField(upload_to='reg_cards',
                                verbose_name="Карточка ККТ",
                                help_text="Прикрепите карточку ККТ",
                                null=True, blank=True)
    legal = models.ForeignKey('Legal', on_delete=models.DO_NOTHING,
                              help_text="Выберите юр. лицо",
                              verbose_name="Юр. лицо, на которое зарегистрирован ФР")
    fn = models.ForeignKey('FiscalStorage', on_delete=models.DO_NOTHING,
                           help_text="Выберите ФН",
                           verbose_name="Фискальный накопитель, установленный в ФР",
                           null=True, blank=True)
    ofd = models.ForeignKey('Ofd', on_delete=models.DO_NOTHING,
                            help_text="Выберите ОФД",
                            verbose_name="ОФД",
                            null=True, blank=True)

    def __str__(self):
        return '%s, %s, ФН %s' % (self.legal, self.rn, self.fn)

    def get_absolute_url(self):
        return reverse('fiscal-reg-detail', args=[str(self.id)])

    class Meta:
        ordering = ['legal']


class Station(models.Model):
    pcname = models.CharField(max_length=20,
                              help_text="Введите имя ПК (необязательно)",
                              verbose_name="Имя ПК",
                              null=True, blank=True)
    stname = models.CharField(max_length=20,
                              help_text="Введите имя как в iiko",
                              verbose_name="Имя станции")
    fr = models.ForeignKey('FiscalRegistrar', on_delete=models.DO_NOTHING,
                           help_text="Выберите ФР, если он(они) подключен к этой станции",
                           verbose_name="Фискальный регистратор",
                           null=True, blank=True)
    printers = models.ManyToManyField('Printers',
                                      help_text="Выберите принтер или принтеры, если они привязаны к это станции",
                                      verbose_name="Принтеры",
                                      null=True, blank=True)
    optequip = models.ManyToManyField('OptEquip',
                                      help_text="Выберите доп оборудование, если оно привязано к это станции",
                                      verbose_name="Доп. оборудование",
                                      null=True, blank=True)
    anylogin = models.CharField(max_length=10,
                                help_text="Введите логин Anydesk",
                                verbose_name="Логин Anydesk")
    anypass = models.CharField(max_length=20,
                               help_text="Введите пароль Anydesk",
                               verbose_name="Пароль Anydesk")
    other = models.CharField(max_length=200,
                             help_text="Добавьте заметку",
                             verbose_name="Примечание",
                             null=True, blank=True)

    def __str__(self):
        return self.stname

    def display_printers(self):
        return ', '.join([printers.stname for printers in self.printers.all()])

    display_printers.short_description = 'Принтеры'

    def display_optequip(self):
        return ', '.join([optequip.stname for optequip in self.optequip.all()])

    display_optequip.short_description = 'Дополнительное оборудование'

    def get_absolute_url(self):
        return reverse('station-detail', args=[str(self.id)])


class Contact(models.Model):
    name = models.CharField(max_length=20,
                            help_text="Введите Имя",
                            verbose_name="Имя")
    last_name = models.CharField(max_length=20,
                                 help_text="Введите фамилию",
                                 verbose_name="Фамилия",
                                 null=True, blank=True)
    phone = models.CharField(max_length=11,
                             help_text="Введите номер телефона (с 7 без +)",
                             verbose_name="Номер телефона")
    telega = models.CharField(max_length=30,
                              help_text="Введите ссылку/логин в Telegram",
                              verbose_name="Telegram",
                              null=True, blank=True)
    other = models.CharField(max_length=200,
                             help_text="Добавьте заметку",
                             verbose_name="Примечание",
                             null=True, blank=True)

    def __str__(self):
        return '%s, %s' % (self.name, self.phone)

    def get_absolute_url(self):
        return reverse('contact-detail', args=[str(self.id)])


class Establishment(models.Model):
    name = models.CharField(max_length=50,
                            help_text="Введите наименование заведения",
                            verbose_name="Заведение")
    stations = models.ManyToManyField('Station',
                                      help_text="Выберите станции, установленные в этом заведении",
                                      verbose_name="Станции")
    address = models.CharField(max_length=50,
                               help_text="Введите адрес заведения",
                               verbose_name="Адрес")
    contact = models.ManyToManyField('Contact',
                                     help_text="Выберите контактное лицо",
                                     verbose_name="Контактное лицо")
    other = models.CharField(max_length=200,
                             help_text="Добавьте заметку",
                             verbose_name="Примечание",
                             null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.name, self.address)

    def display_stations(self):
        return ', '.join([stations.stname for stations in self.stations.all()])

    display_stations.short_description = 'Станции'

    def display_contact(self):
        return ', '.join([contact.stname for contact in self.contact.all()])

    display_contact.short_description = 'Контакты'

    def get_absolute_id(self):
        return reverse('establishment-detail', args=[str(self.id)])


class Corporation(models.Model):
    name = models.CharField(max_length=50,
                            help_text="Введите наименование организации",
                            verbose_name="Организация")
    iiko_server = models.CharField(max_length=50,
                                   help_text="Введите адрес сервера",
                                   verbose_name="Сервер iiko")
    port = models.IntegerField(help_text="Введите порт для подключения",
                               verbose_name="Порт", default="443")
    version = models.ForeignKey('Version', on_delete=models.DO_NOTHING,
                                help_text="Выберите версию iiko",
                                verbose_name="Версия")
    uid = models.CharField(max_length=50,
                           help_text="Введите UID (необязательно)",
                           verbose_name="UID",
                           null=True, blank=True)
    rdp = models.ForeignKey('RDP', on_delete=models.DO_NOTHING,
                            help_text="Выберите RDP если есть",
                            verbose_name="RDP",
                            null=True, blank=True)
    establishments = models.ManyToManyField('Establishment',
                                            help_text='Выберите заведения, входящие в это предприятие',
                                            verbose_name="Список точек")
    other = models.CharField(max_length=200,
                             help_text="Добавьте заметку",
                             verbose_name="Примечание",
                             null=True, blank=True)

    def display_establishments(self):
        return ', '.join([establishments.name for establishments in self.establishments.all()])

    display_establishments.short_description = 'Точки'

    def __str__(self):
        return self.name

    def get_absolute_id(self):
        return reverse('corporation-detail', args=[str(self.id)])


class ModelFiscalRegistrar(models.Model):
    name = models.CharField(max_length=30,
                            help_text="Введите модель ФР",
                            verbose_name="Модель ФР")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class ModelFiscalStorage(models.Model):
    name = models.CharField(max_length=30,
                            help_text="Введите модель Фискального Накопителя",
                            verbose_name="Модель Фискального Накопителя")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
