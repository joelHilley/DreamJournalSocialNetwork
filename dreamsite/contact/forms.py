from django import forms

class Contact(forms.Form):
    Email = forms.EmailField()

    def __str__(self):
        return self.Email