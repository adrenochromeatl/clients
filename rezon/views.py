from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect
from .models import Corporation, Establishment, Station, FiscalRegistrar, FiscalStorage, Contact, Printer, Legal, Ofd, \
    OptEquip, Version, RDP, ModelFiscalRegistrar, ModelFiscalStorage, TypeEq
from django.views.generic import ListView, DetailView
from datetime import datetime
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def index(request):
    time_now = datetime.now()
    text_head = 'Заголовок'
    context = {'text_head': text_head, 'time_now': time_now}
    return render(request, 'directory/index.html', context)


class ContactList(ListView):
    model = Contact
    context_object_name = 'contact'
    template_name = 'directory/list.html'
    paginate_by = 10


class ContactDetail(DetailView):
    model = Contact
    context_object_name = 'contact'
    template_name = 'directory/detail.html'


class ContactCreate(CreateView):
    model = Contact
    context_object_name = 'contact'
    fields = '__all__'
    success_url = reverse_lazy('contact')
    template_name = 'directory/form.html'


class ContactUpdate(UpdateView):
    model = Contact
    context_object_name = 'contact'
    fields = '__all__'
    success_url = reverse_lazy('contact')
    template_name = 'directory/form.html'


class ContactDelete(DeleteView):
    model = Contact
    context_object_name = 'contact'
    success_url = reverse_lazy('contact')
    template_name = 'directory/confirm_delete.html'


class CorporationList(ListView):
    model = Corporation
    context_object_name = 'corporation'
    template_name = 'directory/list.html'
    paginate_by = 10


class CorporationDetail(DetailView):
    model = Corporation
    context_object_name = 'corporation'
    template_name = 'directory/detail.html'


class CorporationCreate(CreateView):
    model = Corporation
    context_object_name = 'corporation'
    fields = '__all__'
    success_url = reverse_lazy('corporation')
    template_name = 'directory/form.html'


class CorporationUpdate(UpdateView):
    model = Corporation
    context_object_name = 'corporation'
    fields = '__all__'
    success_url = reverse_lazy('corporation')
    template_name = 'directory/form.html'


class CorporationDelete(DeleteView):
    model = Corporation
    context_object_name = 'corporation'
    success_url = reverse_lazy('corporation')
    template_name = 'directory/confirm_delete.html'


class EstablishmentList(ListView):
    model = Establishment
    context_object_name = 'establishment'
    template_name = 'directory/list.html'
    paginate_by = 10


class EstablishmentDetail(DetailView):
    model = Establishment
    context_object_name = 'establishment'
    template_name = 'directory/detail.html'


class EstablishmentCreate(CreateView):
    model = Establishment
    context_object_name = 'establishment'
    fields = '__all__'
    success_url = reverse_lazy('establishment')
    template_name = 'directory/form.html'


class EstablishmentUpdate(UpdateView):
    model = Establishment
    context_object_name = 'establishment'
    fields = '__all__'
    success_url = reverse_lazy('establishment')
    template_name = 'directory/form.html'


class EstablishmentDelete(DeleteView):
    model = Establishment
    context_object_name = 'establishment'
    success_url = reverse_lazy('establishment')
    template_name = 'directory/confirm_delete.html'


class FiscalRegistrarList(ListView):
    model = FiscalRegistrar
    context_object_name = 'fiscalregistrar'
    template_name = 'directory/list.html'
    paginate_by = 10


class FiscalRegistrarDetail(DetailView):
    model = FiscalRegistrar
    context_object_name = 'fiscalregistrar'
    template_name = 'directory/detail.html'


class FiscalRegistrarCreate(CreateView):
    model = FiscalRegistrar
    object = 'fiscalregistrar'
    fields = '__all__'
    success_url = reverse_lazy('fiscalregistrar')
    template_name = 'directory/form.html'


class FiscalRegistrarUpdate(UpdateView):
    model = FiscalRegistrar
    context_object_name = 'fiscalregistrar'
    fields = '__all__'
    success_url = reverse_lazy('fiscalregistrar')
    template_name = 'directory/form.html'


class FiscalRegistrarDelete(DeleteView):
    model = FiscalRegistrar
    context_object_name = 'fiscalregistrar'
    success_url = reverse_lazy('fiscalregistrar')
    template_name = 'directory/confirm_delete.html'


class FiscalStorageList(ListView):
    model = FiscalStorage
    context_object_name = 'fiscalstorage'
    template_name = 'directory/list.html'
    paginate_by = 10


class FiscalStorageDetail(DetailView):
    model = FiscalStorage
    context_object_name = 'fiscalstorage'
    template_name = 'directory/detail.html'


class FiscalStorageCreate(CreateView):
    model = FiscalStorage
    context_object_name = 'fiscalstorage'
    fields = '__all__'
    success_url = reverse_lazy('fiscalstorage')
    template_name = 'directory/form.html'


class FiscalStorageUpdate(UpdateView):
    model = FiscalStorage
    context_object_name = 'fiscalstorage'
    fields = '__all__'
    success_url = reverse_lazy('fiscalstorage')
    template_name = 'directory/form.html'


class FiscalStorageDelete(DeleteView):
    model = Establishment
    context_object_name = 'fiscalstorage'
    success_url = reverse_lazy('fiscalstorage')
    template_name = 'directory/confirm_delete.html'


class LegalList(ListView):
    model = Legal
    context_object_name = 'legal'
    template_name = 'directory/list.html'
    paginate_by = 10


class LegalDetail(DetailView):
    model = Legal
    context_object_name = 'legal'
    template_name = 'directory/detail.html'


class LegalCreate(CreateView):
    model = Legal
    context_object_name = 'legal'
    fields = '__all__'
    success_url = reverse_lazy('legal')
    template_name = 'directory/form.html'


class LegalUpdate(UpdateView):
    model = Legal
    context_object_name = 'legal'
    fields = '__all__'
    success_url = reverse_lazy('legal')
    template_name = 'directory/form.html'


class LegalDelete(DeleteView):
    model = Legal
    context_object_name = 'legal'
    success_url = reverse_lazy('legal')
    template_name = 'directory/confirm_delete.html'


class ModelFiscalRegistrarList(ListView):
    model = ModelFiscalRegistrar
    context_object_name = 'modelfiscalregistrar'
    template_name = 'directory/list.html'
    paginate_by = 10


class ModelFiscalRegistrarDetail(DetailView):
    model = ModelFiscalRegistrar
    context_object_name = 'modelfiscalregistrar'
    template_name = 'directory/detail.html'


class ModelFiscalRegistrarCreate(CreateView):
    model = ModelFiscalRegistrar
    context_object_name = 'modelfiscalregistrar'
    fields = '__all__'
    success_url = reverse_lazy('modelfiscalregistrar')
    template_name = 'directory/form.html'


class ModelFiscalRegistrarUpdate(UpdateView):
    model = ModelFiscalRegistrar
    context_object_name = 'modelfiscalregistrar'
    fields = '__all__'
    success_url = reverse_lazy('modelfiscalregistrar')
    template_name = 'directory/form.html'


class ModelFiscalRegistrarDelete(DeleteView):
    model = ModelFiscalRegistrar
    context_object_name = 'modelfiscalregistrar'
    success_url = reverse_lazy('modelfiscalregistrar')
    template_name = 'directory/confirm_delete.html'


class ModelFiscalStorageList(ListView):
    model = ModelFiscalStorage
    context_object_name = 'modelfiscalstorage'
    template_name = 'directory/list.html'
    paginate_by = 10


class ModelFiscalStorageDetail(DetailView):
    model = ModelFiscalStorage
    context_object_name = 'modelfiscalstorage'
    template_name = 'directory/detail.html'


class ModelFiscalStorageCreate(CreateView):
    model = ModelFiscalStorage
    context_object_name = 'modelfiscalstorage'
    fields = '__all__'
    success_url = reverse_lazy('modelfiscalstorage')
    template_name = 'directory/form.html'


class ModelFiscalStorageUpdate(UpdateView):
    model = ModelFiscalStorage
    context_object_name = 'modelfiscalstorage'
    fields = '__all__'
    success_url = reverse_lazy('modelfiscalstorage')
    template_name = 'directory/form.html'


class ModelFiscalStorageDelete(DeleteView):
    model = ModelFiscalStorage
    context_object_name = 'modelfiscalstorage'
    success_url = reverse_lazy('modelfiscalstorage')
    template_name = 'directory/confirm_delete.html'


class OfdList(ListView):
    model = Ofd
    context_object_name = 'ofd'
    template_name = 'directory/list.html'
    paginate_by = 10


class OfdDetail(DetailView):
    model = Ofd
    context_object_name = 'ofd'
    template_name = 'directory/detail.html'


class OfdCreate(CreateView):
    model = Ofd
    context_object_name = 'ofd'
    fields = '__all__'
    success_url = reverse_lazy('ofd')
    template_name = 'directory/form.html'


class OfdUpdate(UpdateView):
    model = Ofd
    context_object_name = 'ofd'
    fields = '__all__'
    success_url = reverse_lazy('ofd')
    template_name = 'directory/form.html'


class OfdDelete(DeleteView):
    model = Ofd
    context_object_name = 'ofd'
    success_url = reverse_lazy('ofd')
    template_name = 'directory/confirm_delete.html'


class OptEquipList(ListView):
    model = OptEquip
    context_object_name = 'optequip'
    template_name = 'directory/list.html'
    paginate_by = 10


class OptEquipDetail(DetailView):
    model = OptEquip
    context_object_name = 'optequip'
    template_name = 'directory/detail.html'


class OptEquipCreate(CreateView):
    model = OptEquip
    context_object_name = 'optequip'
    fields = '__all__'
    success_url = reverse_lazy('optequip')
    template_name = 'directory/form.html'


class OptEquipUpdate(UpdateView):
    model = OptEquip
    context_object_name = 'optequip'
    fields = '__all__'
    success_url = reverse_lazy('optequip')
    template_name = 'directory/form.html'


class OptEquipDelete(DeleteView):
    model = OptEquip
    context_object_name = 'optequip'
    success_url = reverse_lazy('optequip')
    template_name = 'directory/confirm_delete.html'


class PrinterList(ListView):
    model = Printer
    context_object_name = 'printer'
    template_name = 'directory/list.html'
    paginate_by = 10


class PrinterDetail(DetailView):
    model = Printer
    context_object_name = 'printer'
    template_name = 'directory/detail.html'


class PrinterCreate(CreateView):
    model = Printer
    context_object_name = 'printer'
    fields = '__all__'
    success_url = reverse_lazy('printer')
    template_name = 'directory/form.html'


class PrinterUpdate(UpdateView):
    model = Printer
    context_object_name = 'printer'
    fields = '__all__'
    success_url = reverse_lazy('printer')
    template_name = 'directory/form.html'


class PrinterDelete(DeleteView):
    model = Printer
    context_object_name = 'printer'
    success_url = reverse_lazy('printer')
    template_name = 'directory/confirm_delete.html'


class RDPList(ListView):
    model = RDP
    context_object_name = 'rdp'
    template_name = 'directory/list.html'
    paginate_by = 10


class RDPDetail(DetailView):
    model = RDP
    context_object_name = 'rdp'
    template_name = 'directory/detail.html'


class RDPCreate(CreateView):
    model = RDP
    context_object_name = 'rdp'
    fields = '__all__'
    success_url = reverse_lazy('rdp')
    template_name = 'directory/form.html'


class RDPUpdate(UpdateView):
    model = RDP
    context_object_name = 'rdp'
    fields = '__all__'
    success_url = reverse_lazy('rdp')
    template_name = 'directory/form.html'


class RDPDelete(DeleteView):
    model = RDP
    context_object_name = 'rdp'
    success_url = reverse_lazy('rdp')
    template_name = 'directory/confirm_delete.html'


class StationList(ListView):
    model = Station
    context_object_name = 'station'
    template_name = 'directory/list.html'
    paginate_by = 10


class StationDetail(DetailView):
    model = Station
    context_object_name = 'station'
    template_name = 'directory/detail.html'


class StationCreate(CreateView):
    model = Station
    context_object_name = 'station'
    fields = '__all__'
    success_url = reverse_lazy('station')
    template_name = 'directory/form.html'


class StationUpdate(UpdateView):
    model = Station
    context_object_name = 'station'
    fields = '__all__'
    success_url = reverse_lazy('station')
    template_name = 'directory/form.html'


class StationDelete(DeleteView):
    model = Station
    context_object_name = 'station'
    success_url = reverse_lazy('station')
    template_name = 'directory/confirm_delete.html'


class TypeEqList(ListView):
    model = TypeEq
    context_object_name = 'typeeq'
    template_name = 'directory/list.html'
    paginate_by = 10


class TypeEqDetail(DetailView):
    model = TypeEq
    context_object_name = 'typeeq'
    template_name = 'directory/detail.html'


class TypeEqCreate(CreateView):
    model = TypeEq
    context_object_name = 'typeeq'
    fields = '__all__'
    success_url = reverse_lazy('typeeq')
    template_name = 'directory/form.html'


class TypeEqUpdate(UpdateView):
    model = TypeEq
    context_object_name = 'typeeq'
    fields = '__all__'
    success_url = reverse_lazy('typeeq')
    template_name = 'directory/form.html'


class TypeEqDelete(DeleteView):
    model = Station
    context_object_name = 'typeeq'
    success_url = reverse_lazy('typeeq')
    template_name = 'directory/confirm_delete.html'


class VersionList(ListView):
    model = Version
    context_object_name = 'version'
    template_name = 'directory/list.html'
    ordering = ['-name']
    paginate_by = 20


class VersionDetail(DetailView):
    model = Version
    context_object_name = 'version'
    template_name = 'directory/detail.html'


class VersionCreate(CreateView):
    model = Version
    context_object_name = 'version'
    fields = '__all__'
    success_url = reverse_lazy('version')
    template_name = 'directory/form.html'


class VersionUpdate(UpdateView):
    model = Version
    context_object_name = 'version'
    fields = '__all__'
    success_url = reverse_lazy('version')
    template_name = 'directory/form.html'


class VersionDelete(DeleteView):
    model = Version
    context_object_name = 'version'
    success_url = reverse_lazy('version')
    template_name = 'directory/confirm_delete.html'

