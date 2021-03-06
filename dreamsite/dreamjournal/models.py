from django.db import models
from account.models import Account
from django.contrib.auth.models import User
from django.db import models
from multiselectfield import MultiSelectField


# class JournalPostManager(models.Manager):
#     def random(self):
#         count = self.aggregate(count=Count('id'))['count']
#         random_index = randint(0, count - 1)
#         return self.all()[random_index]

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

    #get random JournalPost
    # objects = JournalPostManager()

    username = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='poster')
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    type = models.CharField(blank=True, choices=TYPE_CHOICES, max_length=10)
    category = models.CharField(blank=True, choices=CATEGORY_CHOICES, max_length=15)
    colors_seen = MultiSelectField(blank=True, choices=COLOR_CHOICES)
    privacy = models.IntegerField(choices=PRIVACY_CHOICES, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(Account, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(Account, blank=True, related_name='dislikes')


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post_title = models.ForeignKey(JournalPost, on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='commenter')
    body = models.TextField(max_length=400)
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(JournalPost, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.user)
