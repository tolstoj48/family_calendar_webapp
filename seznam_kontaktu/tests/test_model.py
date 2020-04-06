from django.test import TestCase
from seznam_kontaktu.models import Contact

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Contact.objects.create(first_name="Big", last_name="Bob")

    def test_first_name_label(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_first_name_max_length(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field('first_name').max_length
        self.assertEquals(field_label, 50)

    def test_last_name_label(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'last name')

    def test_last_name_max_length(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field('last_name').max_length
        self.assertEquals(field_label, 50)

    def test_phone_number_label(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field('phone_number').verbose_name
        self.assertEquals(field_label, 'phone number')

    def test_phone_number_max_length(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field('phone_number').max_length
        self.assertEquals(field_label, 20)

    def test_email_label(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')

    def test_email_max_length(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field('email').max_length
        self.assertEquals(field_label, 70)

    def test_object_name(self):
        contact = Contact.objects.get(id=1)
        expected_object_name = f'{contact.first_name}, {contact.last_name}'
        self.assertEquals(expected_object_name, str(contact))

    def test_get_absolute_url(self):
        contact = Contact.objects.get(id=1)
        self.assertEquals(contact.get_absolute_url(), '/edit_contact/1/')
