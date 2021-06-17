from django.contrib import admin
from account.models import Account
from dreamjournal.models import JournalPost

class UserAdmin (admin.ModelAdmin):
    list_display = ('username','email','date_of_birth','sex','nationality','is_superuser','is_admin')
    list_display_links = ('email', 'username')
    list_filter = ('username', 'email')
    search_fields = ('username', 'email', 'nationality')
    list_per_page = 25


class JournalPostAdmin (admin.ModelAdmin):
    list_display = ('title','username','created_at')
    list_display_links = ('title','username','created_at')
    search_fields = ('title','username','created_at')
    list_per_page = 25
    
admin.site.register(Account, UserAdmin)
admin.site.register(JournalPost, JournalPostAdmin)
