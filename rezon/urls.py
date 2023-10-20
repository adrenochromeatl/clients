from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('corporation/', views.CorporationListView.as_view(), name='corporation'),
    path('corporation/<int:pk>/', views.CorporationDetailView.as_view(), name='corporation-detail'),
    path('establishment/', views.EstablishmentListView.as_view(), name='establishment'),
    path('establishment/<int:pk>/', views.EstablishmentDetailView.as_view(), name='establishment-detail'),
    path('station/', views.StationListView.as_view(), name='station'),
    path('station/<int:pk>/', views.StationDetailView.as_view(), name='station-detail'),
]
