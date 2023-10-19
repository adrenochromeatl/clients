from django.shortcuts import render
from .models import Corporation
from django.views.generic import ListView


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
    template_name = 'corporation_list.html'
