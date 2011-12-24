__author__ = 'sam'

from django import forms

class NewsletterSubscription(forms.Form):
    inp_signup_email = forms.EmailField()
