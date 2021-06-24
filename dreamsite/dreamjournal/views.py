from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
from dreamjournal.models import JournalPost, Comment
from account.models import Account
#from . import forms
from dreamjournal.forms import JournalPostForm, CommentForm

# REDUNDANT VIEW
# def home(request):
#     form = JournalPostForm()
#     context = {'form' : form}
#     return render(request, 'home.html', context)

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'home', context)
    else:

        return render(request, 'login.html', context)

# view individual post and related comments
def post_detail(request, id):
    try:
        post = JournalPost.objects.get(id=id)
        comments = Comment.objects.filter(post_title=post).order_by('-id')
    except JournalPost.DoesNotExist:
        raise Http404('Post not found')
    return render(request, 'post_detail.html', {'post': post, 'comments': comments})

#view profile of  users
def user_detail(request, pk):
    profile = Account.objects.get(pk=pk)
    return render(request, 'user_detail.html', {'pk':pk, 'profile':profile})

def profile(request, pk):
    profile = request.user
    post = JournalPost.objects.filter(username_id=pk).order_by('-created_at')
    return render(request, 'profile.html', {'pk': pk, "profile":profile, "post":post})

def add_journal_post(request):
    if request.method == "POST":
        form = JournalPostForm(request.POST)
        poster = request.user
        if form.is_valid():
            instance = form.save(commit=False)
            instance.username = poster
            instance.save()
            form.save()
            return redirect('home')
    else:
        form = JournalPostForm()
    context = {'form' : form}
    return render(request, 'create_post.html', context)

def create_comment(request, id):
    new_comment = None
    post = JournalPost.objects.get(id=id)
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        commenter = request.user
        if form.is_valid():
            # Create Comment object but don't save to database yet
            instance = form.save(commit=False)
            new_comment = form.save(commit=False)
            new_comment.post_title = post
            instance.user = commenter
            instance.save()
            new_comment.save()
            form.save()
            return redirect('home')
    else:
        form = CommentForm()
    return render(request, 'create_comment.html',
    { 'form': form })


from django.views import generic


class PostListView(generic.ListView):
   queryset = JournalPost.objects.filter(privacy=0).order_by('-created_at')
   template_name = 'home.html'


# class PostDetailView(generic.DetailView):
#     model = JournalPost
#     template_name = 'post_detail.html'

from django.views.generic import TemplateView

class AboutPageView(TemplateView):
    template_name = 'about.html'
