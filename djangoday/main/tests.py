"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.core import urlresolvers

from django.test import TestCase
from django.test.client import Client


class SimpleTest(TestCase):
    def test_homepage(self):
         c = Client()
         response = c.get(urlresolvers.reverse('home'))
         self.assertTrue(200,response.status_code)
    def test_newsletter_submission(self):
        c = Client()
        response = c.post(urlresolvers.reverse('subscribe'))
        self.assertTrue(200,response.status_code)

        response = c.post(urlresolvers.reverse('subscribe'), {'inp_signup_email':'fail',})
        self.assertTrue(200,response.status_code)



        self.assertTrue(response.content.count('errorlist') > 0)
        response = c.get(urlresolvers.reverse('subscribe'))
        self.assertTrue(200,response.status_code)
        self.assertTrue(response.content.count('errorlist') == 0)





