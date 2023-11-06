from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect
from .models import Corporation, Establishment, Station, FiscalRegistrar, FiscalStorage, Contact, Printers
from django.views.generic import ListView, DetailView
from datetime import datetime
from .forms import AddCorporation, AddVersion, EditCorporation
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def index(request):
    time_now = datetime.now()
    text_head = 'Заголовок'
    corporations = Corporation.objects.all()
    num_corp = Corporation.objects.all().count()
    context = {'text_head': text_head, 'corporations': corporations,
               'num_corp': num_corp, 'time_now': time_now}
    return render(request, 'rezon/index.html', context)


class CorporationCreate(CreateView):
    model = Corporation
    fields = '__all__'
    success_url = reverse_lazy('corporation')
    template_name = 'rezon/corporation/corporation_form.html'


class CorporationUpdate(UpdateView):
    model = Corporation
    fields = '__all__'
    success_url = reverse_lazy('corporation')
    template_name = 'rezon/corporation/corporation_form.html'


class CorporationDelete(DeleteView):
    model = Corporation
    success_url = reverse_lazy('corporation')
    template_name = 'rezon/corporation/corporation_confirm_delete.html'


class CorporationListView(ListView):
    model = Corporation
    context_object_name = 'corporation'
    template_name = 'rezon/corporation/corporation_list.html'
    paginate_by = 10


class CorporationDetailView(DetailView):
    model = Corporation
    context_object_name = 'corporation'
    template_name = 'rezon/corporation/corporation_detail.html'


class EstablishmentDetailView(DetailView):
    model = Establishment
    context_object_name = 'establishment'
    template_name = 'rezon/establishment/establishment_detail.html'


class EstablishmentListView(ListView):
    model = Establishment
    context_object_name = 'establishment'
    template_name = 'rezon/establishment/establishment_list.html'


class StationDetailView(DetailView):
    model = Station
    context_object_name = 'station'
    template_name = 'rezon/station/station_detail.html'


class FiscalRegistrarListView(ListView):
    model = FiscalRegistrar
    context_object_name = 'fiscalregistrar'
    template_name = 'rezon/fiscalregistrar/fiscalregistrar_list.html'
    paginate_by = 10


class FiscalRegistrarDetailView(DetailView):
    model = FiscalRegistrar
    context_object_name = 'fiscalregistrar'
    template_name = 'rezon/fiscalregistrar/fiscalregistrar_detail.html'


class FRCreate(CreateView):
    model = FiscalRegistrar
    fields = '__all__'
    success_url = reverse_lazy('fr_editor')
    template_name = 'rezon/fiscalregistrar/fiscalregistrar_form.html'


class FRUpdate(UpdateView):
    model = FiscalRegistrar
    fields = '__all__'
    success_url = reverse_lazy('fr_editor')
    template_name = 'rezon/fiscalregistrar/fiscalregistrar_form.html'


class FRDelete(DeleteView):
    model = FiscalRegistrar
    success_url = reverse_lazy('fr_editor')
    template_name = 'rezon/fiscalregistrar/fiscalregistrar_confirm_delete.html'


class FiscalStorageDetailView(DetailView):
    model = FiscalStorage
    context_object_name = 'fiscalstorage'
    template_name = 'rezon/fiscalstorage/fiscalstorage_detail.html'


class ContactDetailView(DetailView):
    model = Contact
    context_object_name = 'contact'
    template_name = 'rezon/contact/contact_detail.html'


class PrinterDetailView(DetailView):
    model = Printers
    context_object_name = 'printers'
    template_name = 'rezon/printers/printers_detail.html'
