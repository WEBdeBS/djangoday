from django.core import urlresolvers
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
import mailchimp
from main.forms import NewsletterSubscription
from main.models import CallForPaper

__author__ = 'sam'


def home(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

def subscribe(request):

    out = {}
    if request.POST:
        form = NewsletterSubscription(request.POST)
        if form.is_valid():
            try:
                list = mailchimp.utils.get_connection().get_list_by_id('160d27d6be')
                list.subscribe(form.cleaned_data['inp_signup_email'],{'EMAIL':form.cleaned_data['inp_signup_email']})
            except Exception as excp:
                    out['form'] = form
                    out['errors'] = unicode(excp)
        else:
            out['form'] = form
            out['errors'] = form.errors
    else:
        form = NewsletterSubscription()
        out['form'] = form
    return render_to_response('subscription.html',out ,context_instance=RequestContext(request))

class CallForPaperView(CreateView):
    template_name = 'cfp.html'
    model = CallForPaper

    def get_success_url(self):
        return urlresolvers.reverse('thanks')

    def post(self, request, *args, **kwargs):
        outcome = super(CallForPaperView).post(request)


class ThanksView(TemplateView):
    template_name = 'thanks.html'

