from django.contrib import admin
from account.models import Account
from dreamjournal.models import JournalPost, Comment

class UserAdmin (admin.ModelAdmin):
    list_display = ('id','username','email','date_of_birth','age','sex','nationality','is_superuser','is_admin')
    list_display_links = ('email', 'username')
    list_filter = ('username', 'email')
    search_fields = ('username', 'email', 'nationality')
    list_per_page = 25


class JournalPostAdmin (admin.ModelAdmin):
    list_display = ('title','username','created_at')
    list_display_links = ('title','username','created_at')
    search_fields = ('title','username','created_at')
    list_per_page = 25


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post_title', 'created_on')
    list_filter = ('user', 'created_on')
    search_fields = ('user', 'body')

class ConversationAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_on')
    list_filter = ('user', 'created_on')
    search_fields = ('user', 'created_on')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'message')
    list_filter = ('sender', 'recipient')
    search_fields = ('sender', 'recipient')


admin.site.register(Account, UserAdmin)
admin.site.register(JournalPost, JournalPostAdmin)
admin.site.register(Comment, CommentAdmin)
