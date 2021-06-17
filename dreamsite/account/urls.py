from django.urls import path

from . import views
from .views import signup_view

app_name = 'account'

urlpatterns = [
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup_view, name='signup'),
]
