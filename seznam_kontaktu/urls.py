from django.urls import path
from . import views

app_name = 'seznam_kontaktu'
urlpatterns = [
    path('list_contacts/', views.ContactsListView.as_view(), name = 'list_contacts'),
    path('new_contact/', views.NewContactView.as_view(), name='new_contact'),
    path('edit_contact/<int:pk>/', views.EditContactView.as_view(), name='edit_contact'),
    path('delete_contact/<int:pk>/', views.DeleteContactView.as_view(), name = 'delete_contact'),
]