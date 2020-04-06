from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView, CreateView
from django.views.generic import UpdateView
from django.urls import reverse_lazy

from .models import *

class ContactsListView(LoginRequiredMixin, ListView):
    model = Contact
    template_name = 'contacts/contacts_list.html'
    context_object_name = 'contacts'

class NewContactView(LoginRequiredMixin, CreateView):
    model = Contact
    template_name = 'contacts/contact.html'
    fields = ['first_name','last_name', 'phone_number', 'email',]
    success_url = reverse_lazy('seznam_kontaktu:list_contacts')

class EditContactView(LoginRequiredMixin, UpdateView):
    model = Contact
    template_name = 'contacts/contact.html'
    fields = ['first_name','last_name', 'phone_number', 'email',]
    success_url = reverse_lazy('seznam_kontaktu:list_contacts')

    def get_queryset(self):
        kontakt_id = self.kwargs['pk']
        new_context = Contact.objects.filter(pk=kontakt_id)
        return new_context

class DeleteContactView(LoginRequiredMixin, DeleteView):
    model = Contact
    template_name = 'contacts/contact_delete.html'
    success_url = reverse_lazy('seznam_kontaktu:list_contacts')