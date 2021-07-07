from django import forms

class ConversationForm(forms.Form):
    username = forms.CharField(label='', max_length = 25)

class MessageForm(forms.Form):
    message = forms.CharField(label='', max_length = 800)
