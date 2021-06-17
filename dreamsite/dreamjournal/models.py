from django.db import models
from account.models import Account
from multiselectfield import MultiSelectField

class JournalPost(models.Model):
    TYPE_CHOICES = [
    ('Dream', 'Dream'),
    ('Nightmare', 'Nightmare')
    ]
#add field for users to enter a category
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

    username = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField(max_length=500)
    type = models.CharField(blank=True, choices=TYPE_CHOICES, max_length=10)
    category = models.CharField(blank=True, choices=CATEGORY_CHOICES, max_length=15)
    colors_seen = MultiSelectField(blank=True, choices=COLOR_CHOICES)
    likes = models.IntegerField(default=0)
    privacy = models.IntegerField(choices=PRIVACY_CHOICES, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
