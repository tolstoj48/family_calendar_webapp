from django.test import TestCase, Client
from seznam_kontaktu.models import Contact
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.

def login(client):
    '''Helper function - login.'''
    credentials = {
            'username': "karel",
            'password': "foo",
        }
    return client.post('/accounts/login/', credentials, follow=True)

def setup_user():
    '''Helper function - user creation'''
    User = get_user_model()
    user = User.objects.create_user(username="karel", email='normal@user.com', password='foo')
    return user

def create_contact_object():
    return Contact.objects.create(first_name="Petr", last_name="Musil", phone_number="777", email="petr@petr.cz")

class ContactModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        contact = Contact.objects.create(first_name="Petr", last_name="Musil", phone_number="777", email="petr@petr.cz")

    def setUp(self):
        user = setup_user()

    def test_contact_content(self):
        contact = Contact.objects.get(id=1)
        expected_first_name = f'{contact.first_name}'
        expected_last_name = f'{contact.last_name}'
        expected_phone = f'{contact.phone_number}'
        expected_mail =  f'{contact.email}'
        self.assertEqual(expected_first_name, 'Petr')
        self.assertEqual(expected_last_name, 'Musil')
        self.assertEqual(expected_phone, '777')
        self.assertEqual(expected_mail, 'petr@petr.cz')
        

class ContactsListViewTests(TestCase):
    def setUp(self):
        user = setup_user()
        login(self.client)

    def test_contacts_list_status_code(self):
        response = self.client.get('/list_contacts/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('seznam_kontaktu:list_contacts'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('seznam_kontaktu:list_contacts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacts/contacts_list.html')

class NewContactViewTest(TestCase):
    def setUp(self):
        user = setup_user()
        login(self.client)

    def test_contact_new_exists_proper_url(self):
        response = self.client.get('/new_contact/')
        self.assertEqual(response.status_code, 200)

    def test_contact_new_url_by_name(self):
        response = self.client.get(reverse('seznam_kontaktu:new_contact'))
        self.assertEqual(response.status_code, 200)

    def test_contact_new_uses_correct_template(self):
        response = self.client.get(reverse('seznam_kontaktu:new_contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacts/contact.html')

class EditContactViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        contact = Contact.objects.create(first_name="Petr", last_name="Musil", phone_number="777", email="petr@petr.cz")

    def setUp(self):
        user = setup_user()
        login(self.client)

    def test_contact_detail_exists_proper_url(self):
        response = self.client.get('/edit_contact/3/')
        self.assertEqual(response.status_code, 200)

    def test_contact_detail_url_by_name(self):
        response = self.client.get(reverse('seznam_kontaktu:edit_contact', args=(3,)), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_contact_detail_uses_correct_template(self):
        response = self.client.get(reverse('seznam_kontaktu:edit_contact',args=(3,)), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacts/contact.html')

class DeleteContactViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        contact = Contact.objects.create(first_name="Petr", last_name="Musil", phone_number="777", email="petr@petr.cz")

    def setUp(self):
        user = setup_user()
        self.client = Client()
        login(self.client)


    def test_contactdelete(self):
        post_response = self.client.post(reverse('seznam_kontaktu:delete_contact', args=(2,)), follow=True)
        self.assertRedirects(post_response, '/list_contacts/', status_code=302)
        self.assertFalse(Contact.objects.filter(pk=2).exists())