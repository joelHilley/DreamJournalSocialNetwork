from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

class HomePage(TemplateView):
  template_view = 'home.html'
#about page view
class AboutPage(TemplateView):
  template_name = 'about.html'

class LoginPage(TemplateView):
  template_name = 'login.html'

class InboxPage(TemplateView):
  template_name = 'inbox.html'
