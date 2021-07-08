from django.contrib import admin
from messenger.models import Conversation, Message


# Register your models here.
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('user', 'receiver', 'created_on')
    list_filter = ('user', 'created_on')
    search_fields = ('user', 'created_on')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'message')
    list_filter = ('sender', 'recipient')
    search_fields = ('sender', 'recipient')


admin.site.register(Conversation, ConversationAdmin)
admin.site.register(Message, MessageAdmin)
