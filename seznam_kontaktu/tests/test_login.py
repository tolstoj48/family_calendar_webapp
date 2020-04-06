from django.test import override_settings,TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

@override_settings(AXES_ENABLED=False)
class LoginListViewTest(TestCase):
    def setUp(self):
        test_user1 = User.objects.create_user(username='testuser1', email='normal@user.com', password='1X<ISRUkw+tuK')
        test_user1.save()
        self.client = Client()

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('seznam_kontaktu:list_contacts'))
        self.assertRedirects(response, '/accounts/login/?next=/list_contacts/')

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('seznam_kontaktu:list_contacts'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacts/contacts_list.html')
