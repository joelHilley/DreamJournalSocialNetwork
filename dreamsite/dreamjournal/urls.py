from django.urls import path, include
from .views import AboutPageView, home
from . import views


urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('post_detail/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('user_detail/<str:username_id>', views.UserDetailView.as_view(), name='user_detail'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('create_post/', views.add_journal_post, name='create_post')
]
