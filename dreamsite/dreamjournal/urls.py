from django.urls import path, include
from .views import AboutPageView, user_detail, post_detail, profile, AddLike, AddDislike, search, UpdatePostView, DeletePostView
from . import views
from messenger.views import ListConversations, CreateConversation


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
    # search posts content
    path('search/', search, name='search'),
    # edit and delete posts
    path('post_detail/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('post_detail/delete/<int:pk>', DeletePostView.as_view(), name='delete_post'),
    path('', include(('messenger.urls', 'inbox'), namespace='messenger')),
    path('inbox/', ListConversations.as_view(), name='inbox'),
    path('inbox/new_convo', CreateConversation.as_view(), name='new_convo'),
]
