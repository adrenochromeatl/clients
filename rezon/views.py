from django.shortcuts import render
from .models import Corporation


def index(request):
    text_head = 'Заголовок'
    corporations = Corporation.objects.all()
    num_corp = Corporation.objects.all().count()
    context = {'text_head': text_head, 'corporations': corporations,
               'num_corp': num_corp}
    return render(request, 'rezon/index.html', context)
