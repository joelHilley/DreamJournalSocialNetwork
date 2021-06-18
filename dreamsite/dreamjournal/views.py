from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
from dreamjournal.models import JournalPost
from account.models import Account
from . import forms
from dreamjournal.forms import JournalPostForm


def home(request):
    form = JournalPostForm()
    context = {'form' : form}
    return render(request, 'home.html', context)

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'home', context)
    else:

        return render(request, 'login.html', context)

#view comments and post in detail
def post_detail(request, id):
    try:
        post = JournalPost.objects.get(id=id)
    except JournalPost.DoesNotExist:
        raise Http404('Post not found')
    return render(request, 'post_detail.html', {'post': post})

#View profile of another user
def user_detail(request, id):
    try:
        user = Account.objects.get(id=id)
    except Account.DoesNotExist:
        raise Http404('Post not found')
    return render(request, 'user_detail.html', {'user': user})

def add_journal_post(request):
    if request.method == "POST":
        form = JournalPostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user.username
            instance.save()
            form.save()
            return redirect('home')
    else:
        form = JournalPostForm()
    context = {'form' : form}
    return render(request, 'create_post.html', context)

from django.views import generic

class PostListView(generic.ListView):
   queryset = JournalPost.objects.filter(privacy=0).order_by('-created_at')
   template_name = 'home.html'

class PostDetailView(generic.DetailView):
    model = JournalPost
    template_name = 'post_detail.html'

class UserDetailView(generic.DetailView):
    model = JournalPost
    pk_url_kwarg = 'username_id' #changes url requirement from primary key to  username_id
    template_name = 'user_detail.html'

from django.views.generic import TemplateView

class AboutPageView(TemplateView):
    template_name = 'about.html'
