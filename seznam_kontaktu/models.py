from django.urls import reverse
from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=70)

    def get_absolute_url(self):
        return reverse('seznam_kontaktu:edit_contact', args=[str(self.id,)])

    def __str__(self):
        return f'{self.id}, {self.first_name}, {self.last_name}'