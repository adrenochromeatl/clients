from django.contrib import admin
from django.utils.html import format_html
from .models import Corporation, Establishment, Station, \
    TypeEq, Contact, Version, RDP, FiscalRegistrar, Printer, \
    OptEquip, FiscalStorage, Ofd, Legal, ModelFiscalStorage, ModelFiscalRegistrar


class CorporationAdmin(admin.ModelAdmin):
    list_display = ('name', 'version', 'display_establishments')
    list_filter = ('name', 'version')
    fields = ['name', ('iiko_server', 'port', 'rdp'), ('version', 'uid'), 'establishments', 'other']


admin.site.register(Corporation, CorporationAdmin)


class EstablishmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    list_filter = ('name', 'address')


admin.site.register(Establishment, EstablishmentAdmin)


class StationAdmin(admin.ModelAdmin):
    list_display = ('stname', 'pcname', 'anylogin', 'anypass')
    list_filter = ('stname', 'pcname')


admin.site.register(Station, StationAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'name', 'phone', 'telega')
    list_filter = ('last_name', 'phone')


admin.site.register(Contact, ContactAdmin)


class FiscalRegistrarAdmin(admin.ModelAdmin):
    list_display = ('legal', 'rn', 'zn', 'model', 'ofd')
    list_filter = ('legal', 'model', 'ofd')


admin.site.register(FiscalRegistrar, FiscalRegistrarAdmin)


class PrinterAdmin(admin.ModelAdmin):
    list_display = ('name', 'model')


admin.site.register(Printer, PrinterAdmin)


class OptEquipAdmin(admin.ModelAdmin):
    list_display = ('type_equip', 'model')
    list_filter = ('type_equip',)


admin.site.register(OptEquip, OptEquipAdmin)


class FiscalStorageAdmin(admin.ModelAdmin):
    list_display = ('number', 'validity', 'model')
    list_filter = ('number', 'validity', 'model')


admin.site.register(FiscalStorage, FiscalStorageAdmin)

admin.site.register(Ofd)
admin.site.register(Legal)
admin.site.register(RDP)
admin.site.register(TypeEq)
admin.site.register(Version)
admin.site.register(ModelFiscalStorage)
admin.site.register(ModelFiscalRegistrar)
