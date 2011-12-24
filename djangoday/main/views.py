from django.shortcuts import render_to_response
from django.template.context import RequestContext
import mailchimp
from main.forms import NewsletterSubscription

__author__ = 'sam'


def home(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

def subscribe(request):

    out = {}
    if request.POST:
        form = NewsletterSubscription(request.POST)
        if form.is_valid():
            list = mailchimp.utils.get_connection().get_list_by_id('160d27d6be')
            list.subscribe(form.cleaned_data['inp_signup_email'],{'EMAIL':form.cleaned_data['inp_signup_email']})
        else:
            out['form'] = form
    else:
        form = NewsletterSubscription()
        out['form'] = form
    return render_to_response('subscription.html',out ,context_instance=RequestContext(request))
