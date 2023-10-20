from django.shortcuts import render
from .models import Corporation, Establishment, Station
from django.views.generic import ListView, DetailView


def index(request):
    text_head = 'Заголовок'
    corporations = Corporation.objects.all()
    num_corp = Corporation.objects.all().count()
    context = {'text_head': text_head, 'corporations': corporations,
               'num_corp': num_corp}
    return render(request, 'rezon/index.html', context)


class CorporationListView(ListView):
    model = Corporation
    context_object_name = 'corporation'


class CorporationDetailView(DetailView):
    model = Corporation
    context_object_name = 'corporation'


class EstablishmentListView(ListView):
    model = Establishment
    context_object_name = 'establishment'


class EstablishmentDetailView(DetailView):
    model = Establishment
    context_object_name = 'establishment'


class StationListView(ListView):
    model = Station
    context_object_name = 'station'


class StationDetailView(DetailView):
    model = Station
    context_object_name = 'station'
