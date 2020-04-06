from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from seznam_kontaktu.models import Contact

#testing url exists, reverse, correct template, 

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

class ContactListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_contacts = 13

        for contact_id in range(number_of_contacts):
            Contact.objects.create(
                first_name=f'Christian {contact_id}',
                last_name=f'Surname {contact_id}',
                phone_number=f'777 {contact_id}',
                email = f'p@g.cz'
            )
    def setUp(self):
        user = setup_user()
        self.client = Client()
        login(self.client)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/list_contacts/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('seznam_kontaktu:list_contacts'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('seznam_kontaktu:list_contacts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacts/contacts_list.html')

class NewContactViewTest(TestCase):
    def setUp(self):
        user = setup_user()
        self.client = Client()
        login(self.client)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/new_contact/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('seznam_kontaktu:new_contact'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('seznam_kontaktu:new_contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacts/contact.html')

    def test_form_post_correctly(self):
        response = self.client.post(reverse('seznam_kontaktu:new_contact'), {'first_name': 'See','last_name': 'Mall', 'phone_number': '666', 'email': 'g@g.cz'})
        self.assertEqual(response.status_code, 302)
        response_after_create = self.client.get(response.url)
        self.assertContains(response_after_create, "Mall")

class EditContactViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_contacts = 1

        for contact_id in range(number_of_contacts):
            Contact.objects.create(
                first_name=f'Christian {contact_id}',
                last_name=f'Surname {contact_id}',
                phone_number=f'777 {contact_id}',
                email = f'p@g.cz'
            )
    def setUp(self):
        user = setup_user()
        self.client = Client()
        login(self.client)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/edit_contact/1/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('seznam_kontaktu:edit_contact', args=(1,)))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('seznam_kontaktu:edit_contact', args=(1,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacts/contact.html')

    def test_edit_contact_data(self):
        response = self.client.post(reverse('seznam_kontaktu:edit_contact', args='1'), {'last_name': 'Mus', 'email': 'h@g.cz'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Mus")
        self.assertContains(response, "h@g.cz")

class DeleteContactViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_contacts = 1

        for contact_id in range(number_of_contacts):
            Contact.objects.create(
                first_name=f'Christian {contact_id}',
                last_name=f'Surname {contact_id}',
                phone_number=f'777 {contact_id}',
                email = f'p@g.cz'
            )
    def setUp(self):
        user = setup_user()
        self.client = Client()
        login(self.client)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/delete_contact/1/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('seznam_kontaktu:delete_contact', args=(1,)), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('seznam_kontaktu:delete_contact', args=(1,)), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacts/contact_delete.html')