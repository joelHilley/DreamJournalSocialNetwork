from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

class LoginPage(TemplateView):
  template_name = 'login.html'
