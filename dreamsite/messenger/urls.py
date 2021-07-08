from django.urls import path, include
from .views import ListConversations, CreateConversation
from . import views

app_name = 'messenger'

urlpatterns = [
    # path('inbox/', ListConversations.as_view(), name='inbox'),
    # path('inbox/new_convo', CreateConversation.as_view(), name='new_convo'),

]
