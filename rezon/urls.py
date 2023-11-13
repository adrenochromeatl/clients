from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.ContactList.as_view(), name='contact'),
    path('contact/<int:pk>/', views.ContactDetail.as_view(), name='contact-detail'),
    path('contact/create/', views.ContactCreate.as_view(), name='contact-create'),
    path('contact/update/<int:pk>', views.ContactUpdate.as_view(), name='contact-update'),
    path('contact/delete/<int:pk>', views.ContactDelete.as_view(), name='contact-delete'),
    path('corporation/', views.CorporationList.as_view(), name='corporation'),
    path('corporation/<int:pk>/', views.CorporationDetail.as_view(), name='corporation-detail'),
    path('corporation/create/', views.CorporationCreate.as_view(), name='corporation-create'),
    path('corporation/update/<int:pk>', views.CorporationUpdate.as_view(), name='corporation-update'),
    path('corporation/delete/<int:pk>', views.CorporationDelete.as_view(), name='corporation-delete'),
    path('establishment/', views.EstablishmentList.as_view(), name='establishment'),
    path('establishment/<int:pk>/', views.EstablishmentDetail.as_view(), name='establishment-detail'),
    path('establishment/create/', views.EstablishmentCreate.as_view(), name='establishment-create'),
    path('establishment/update/<int:pk>', views.EstablishmentUpdate.as_view(), name='establishment-update'),
    path('establishment/delete/<int:pk>', views.EstablishmentDelete.as_view(), name='establishment-delete'),
    path('fiscalregistrar/', views.FiscalRegistrarList.as_view(), name='fiscalregistrar'),
    path('fiscalregistrar/<int:pk>/', views.FiscalRegistrarDetail.as_view(), name='fiscalregistrar-detail'),
    path('fiscalregistrar/create/', views.FiscalStorageCreate.as_view(), name='fiscalregistrar-create'),
    path('fiscalregistrar/update/<int:pk>/', views.FiscalStorageUpdate.as_view(), name='fiscalregistrar-update'),
    path('fiscalregistrar/delete/<int:pk>/', views.FiscalStorageDelete.as_view(), name='fiscalregistrar-delete'),
    path('fiscalstorage/', views.FiscalStorageList.as_view(), name='fiscalstorage'),
    path('fiscalstorage/<int:pk>/', views.FiscalStorageDetail.as_view(), name='fiscalstorage-detail'),
    path('fiscalstorage/create/', views.FiscalStorageCreate.as_view(), name='fiscalstorage-create'),
    path('fiscalstorage/update/<int:pk>', views.FiscalStorageUpdate.as_view(), name='fiscalstorage-update'),
    path('fiscalstorage/delete/<int:pk>', views.FiscalStorageDelete.as_view(), name='fiscalstorage-delete'),
    path('legal/', views.LegalList.as_view(), name='legal'),
    path('legal/<int:pk>/', views.LegalDetail.as_view(), name='legal-detail'),
    path('legal/create/', views.LegalCreate.as_view(), name='legal-create'),
    path('legal/update/<int:pk>', views.LegalUpdate.as_view(), name='legal-update'),
    path('legal/delete/<int:pk>', views.LegalDelete.as_view(), name='legal-delete'),
    path('modelfiscalregistrar/', views.ModelFiscalRegistrarList.as_view(), name='modelfiscalregistrar'),
    path('modelfiscalregistrar/<int:pk>/', views.ModelFiscalRegistrarDetail.as_view(), name='modelfiscalregistrar'
                                                                                            '-detail'),
    path('modelfiscalregistrar/create/', views.ModelFiscalRegistrarCreate.as_view(), name='modelfiscalregistrar'
                                                                                          '-create'),
    path('modelfiscalregistrar/update/<int:pk>', views.ModelFiscalRegistrarUpdate.as_view(), name='modelfiscalregistrar'
                                                                                                  '-update'),
    path('modelfiscalregistrar/delete/<int:pk>', views.ModelFiscalRegistrarDelete.as_view(), name='modelfiscalregistrar'
                                                                                                  '-delete'),
    path('modelfiscalstorage/', views.ModelFiscalStorageList.as_view(), name='modelfiscalstorage'),
    path('modelfiscalstorage/<int:pk>/', views.ModelFiscalStorageDetail.as_view(), name='modelfiscalstorage-detail'),
    path('modelfiscalstorage/create/', views.ModelFiscalStorageCreate.as_view(), name='modelfiscalstorage-create'),
    path('modelfiscalstorage/update/<int:pk>', views.ModelFiscalStorageUpdate.as_view(), name='modelfiscalstorage'
                                                                                              '-update'),
    path('modelfiscalstorage/delete/<int:pk>', views.ModelFiscalStorageDelete.as_view(), name='modelfiscalstorage'
                                                                                              '-delete'),
    path('ofd/', views.OfdList.as_view(), name='ofd'),
    path('ofd/<int:pk>/', views.OfdDetail.as_view(), name='ofd-detail'),
    path('ofd/create/', views.OfdCreate.as_view(), name='ofd-create'),
    path('ofd/update/<int:pk>', views.OfdUpdate.as_view(), name='ofd-update'),
    path('ofd/delete/<int:pk>', views.OfdDelete.as_view(), name='ofd-delete'),
    path('optequip/', views.OptEquipList.as_view(), name='optequip'),
    path('optequip/<int:pk>/', views.OptEquipDetail.as_view(), name='optequip-detail'),
    path('optequip/create/', views.OptEquipCreate.as_view(), name='optequip-create'),
    path('optequip/update/<int:pk>', views.OptEquipUpdate.as_view(), name='optequip-update'),
    path('optequip/delete/<int:pk>', views.OptEquipDelete.as_view(), name='optequip-delete'),
    path('printer/', views.PrinterList.as_view(), name='printer'),
    path('printer/<int:pk>/', views.PrinterDetail.as_view(), name='printer-detail'),
    path('printer/create/', views.PrinterCreate.as_view(), name='printer-create'),
    path('printer/update/<int:pk>', views.PrinterUpdate.as_view(), name='printer-update'),
    path('printer/delete/<int:pk>', views.PrinterDelete.as_view(), name='printer-delete'),
    path('rdp/', views.RDPList.as_view(), name='rdp'),
    path('rdp/<int:pk>/', views.RDPDetail.as_view(), name='rdp-detail'),
    path('rdp/create/', views.RDPCreate.as_view(), name='rdp-create'),
    path('rdp/update/<int:pk>', views.RDPUpdate.as_view(), name='rdp-update'),
    path('rdp/delete/<int:pk>', views.RDPDelete.as_view(), name='rdp-delete'),
    path('station/', views.StationList.as_view(), name='station'),
    path('station/<int:pk>/', views.StationDetail.as_view(), name='station-detail'),
    path('station/create/', views.StationCreate.as_view(), name='station-create'),
    path('station/update/<int:pk>', views.StationUpdate.as_view(), name='station-update'),
    path('station/delete/<int:pk>', views.StationDelete.as_view(), name='station-delete'),
    path('typeeq/', views.TypeEqList.as_view(), name='typeeq'),
    path('typeeq/<int:pk>/', views.TypeEqDetail.as_view(), name='typeeq-detail'),
    path('typeeq/create/', views.TypeEqCreate.as_view(), name='typeeq-create'),
    path('typeeq/update/<int:pk>', views.TypeEqUpdate.as_view(), name='typeeq-update'),
    path('typeeq/delete/<int:pk>', views.TypeEqDelete.as_view(), name='typeeq-delete'),
    path('version/', views.VersionList.as_view(), name='version'),
    path('version/<int:pk>/', views.VersionDetail.as_view(), name='version-detail'),
    path('version/create/', views.VersionCreate.as_view(), name='version-create'),
    path('version/update/<int:pk>', views.VersionUpdate.as_view(), name='version-update'),
    path('version/delete/<int:pk>', views.VersionDelete.as_view(), name='version-delete'),
]
