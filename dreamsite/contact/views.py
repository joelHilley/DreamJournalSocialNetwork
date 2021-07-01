from django.shortcuts import render
from dreamsite.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import message, send_mail

# Create your views here.
# Dream Catcher #Send Email
def contact(request):
    sub = forms.Contact()
    if request.method == 'POST' :
        sub = forms.Contact(request.POST)
        subject = 'Welcome to Dream Catcher'
        message = 'Hope you are enjoy our application'
        recepient = str(sub['Email'].value())
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'contact/success.html',{'recepient': recepient}) 
    return render(request, 'contact/index.html', {'form' :sub})
