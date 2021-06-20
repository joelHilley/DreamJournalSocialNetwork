from django.forms import ModelForm
from dreamjournal.models import JournalPost, Comment
#from multiselectfield import MultiSelectField
from django import forms

class JournalPostForm(ModelForm):
    class Meta:
        TYPE_CHOICES = [
        ('Dream', 'Dream'),
        ('Nightmare', 'Nightmare')
        ]

        CATEGORY_CHOICES = [
        ('Reality','Reality'),
        ('Fantasy/Unreal', 'Fantasy/Unreal')
        ]

        COLOR_CHOICES = [
        ('Red','Red'),
        ('Blue','Blue'),
        ('Yellow','Yellow'),
        ('Green','Green'),
        ('Orange','Orange'),
        ('Violet','Violet'),
        ('Brown','Brown'),
        ('Black','Black'),
        ('White','White'),
        ]

        PRIVACY_CHOICES = [
        (0,'Public'),
        (1,'Private')
        ]
        model = JournalPost
        #colors_seen = MultiSelectField(choices=COLOR_CHOICES)
        #type = forms.ChoiceField(choices=TYPE_CHOICES, widget=forms.RadioSelect)
        #category = forms.ChoiceField(choices=CATEGORY_CHOICES, widget=forms.RadioSelect)
        #privacy = forms.ChoiceField(choices=PRIVACY_CHOICES, widget=forms.RadioSelect)

        fields = ['title', 'content', 'type', 'category', 'colors_seen', 'privacy']
        #exclude = ['username', 'likes', 'created_at', 'updated_at']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
