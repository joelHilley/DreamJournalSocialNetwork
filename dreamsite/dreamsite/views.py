from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

class HomePage(TemplateView):
  template_view = 'home.html'

#terms and conditions view
# class AboutPage(TemplateView):
#   template_name = 'terms.html'  

#about page view
class AboutPage(TemplateView):
  template_name = 'about.html'

class LoginPage(TemplateView):
  template_name = 'login.html'
