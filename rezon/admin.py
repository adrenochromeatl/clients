from django.contrib import admin
from .models import Corporation, Establishment, Station, \
    TypeEq, Contact, Version, RDP, FiscalRegistrar, Printers, \
    OptEquip, FiscalStorage, Ofd, Legal

admin.site.register(Corporation)
admin.site.register(Establishment)
admin.site.register(Station)
admin.site.register(TypeEq)
admin.site.register(Contact)
admin.site.register(Version)
admin.site.register(RDP)
admin.site.register(FiscalRegistrar)
admin.site.register(Printers)
admin.site.register(OptEquip)
admin.site.register(FiscalStorage)
admin.site.register(Ofd)
admin.site.register(Legal)
