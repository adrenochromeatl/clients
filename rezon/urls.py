from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('corporation/', views.CorporationListView.as_view(), name='corporation'),
    path('corporation/<int:pk>/', views.CorporationDetailView.as_view(), name='corporation-detail'),
    path('corporation/create/', views.CorporationCreate.as_view(), name='corporation-create'),
    path('corporation/update/<int:pk>', views.CorporationUpdate.as_view(), name='corporation-update'),
    path('corporation/delete/<int:pk>', views.CorporationDelete.as_view(), name='corporation-delete'),
    path('establishment/<int:pk>/', views.EstablishmentDetailView.as_view(), name='establishment-detail'),
    path('station/<int:pk>/', views.StationDetailView.as_view(), name='station-detail'),
    path('fiscalregistrar/', views.FiscalRegistrarListView.as_view(), name='fiscalregistrar'),
    path('fiscalregistrar/<int:pk>/', views.FiscalRegistrarDetailView.as_view(), name='fiscalregistrar-detail'),
    path('fiscalregistrar/create/', views.FRCreate.as_view(), name='fiscalregistrar-create'),
    path('fiscalregistrar/update/<int:pk>/', views.FRUpdate.as_view(), name='fiscalregistrar-update'),
    path('fiscalregistrar/delete/<int:pk>/', views.FRDelete.as_view(), name='fiscalregistrar-delete'),
    path('fiscalstorage/<int:pk>/', views.FiscalStorageDetailView.as_view(), name='fiscalstorage-detail'),
    path('contact/<int:pk>/', views.ContactDetailView.as_view(), name='contact-detail'),
    path('printer/<int:pk>/', views.PrinterDetailView.as_view(), name='printers-detail'),
]
