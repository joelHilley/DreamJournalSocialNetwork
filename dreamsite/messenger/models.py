from django.db import models
from account.models import Account
# from django.contrib.auth.models import User


# Create your models here.
class Conversation(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='user')
    receiver = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='receiver')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

class Message(models.Model):
    convo = models.ForeignKey(Conversation, on_delete=models.CASCADE,related_name='convo')
    sender = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='sender')
    recipient = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='recipient')
    message = models.TextField(max_length=800)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Comment {} by {}'.format(self.message, self.sender)
