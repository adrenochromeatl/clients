from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('corporation/', views.CorporationListView.as_view(), name='corporation')
]