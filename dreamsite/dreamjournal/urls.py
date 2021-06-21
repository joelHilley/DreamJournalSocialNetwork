from django.urls import path, include
from .views import AboutPageView, user_detail, post_detail
from . import views


urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('post_detail/<int:id>', post_detail, name='post_detail'),
    path('user/<int:pk>', user_detail, name='user_detail'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('create_post/', views.add_journal_post, name='create_post'),
    path('create_comment/', views.create_comment, name='create_comment')
]
