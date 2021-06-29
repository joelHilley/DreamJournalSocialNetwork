from django.urls import path, include
from .views import AboutPageView, user_detail, post_detail, profile
from . import views


urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('nightmare/', views.NightmareListView.as_view(), name='nightmare'),
    path('dream/', views.DreamListView.as_view(), name='dream'),
    path('reality/', views.RealityListView.as_view(), name='reality'),
    path('fantasy/', views.FantasyListView.as_view(), name='fantasy'),
    path('post_detail/<int:id>', post_detail, name='post_detail'),
    path('user/<int:pk>', user_detail, name='user_detail'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('create_post/', views.add_journal_post, name='create_post'),
    path('create_comment/<int:id>', views.create_comment, name='create_comment'),
    path('profile/<int:pk>', profile, name='profile'),
    # added for likes and dislikes function
    path('post/<int:pk>/like', AddLike.as_view(), name='like'),
    path('post/<int:pk>/dislike', AddDislike.as_view(), name='dislike'),
]
