from django.views import generic
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView, UpdateView, DeleteView
from dreamjournal.models import JournalPost, Comment
from account.models import Account
#from . import forms
from dreamjournal.forms import JournalPostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views import View


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
@login_required
def post_detail(request, id):
    try:
        post = JournalPost.objects.get(id=id)
        comments = Comment.objects.filter(post_title=post).order_by('-id')
    except JournalPost.DoesNotExist:
        raise Http404('Post not found')
    return render(request, 'post_detail.html', {'post': post, 'comments': comments,})

#view profile of  users
@login_required
def user_detail(request, pk):
    profile = Account.objects.get(pk=pk)
    posts = JournalPost.objects.filter(username_id=pk).order_by('-created_at')
    me = request.user
    return render(request, 'user_detail.html', {'pk':pk, 'profile':profile, 'posts':posts, 'me':me})

def profile(request, pk):
    profile = request.user
    posts = JournalPost.objects.filter(username_id=pk).order_by('-created_at')
    return render(request, 'profile.html', {'pk': pk, "profile":profile, "posts":posts})

@login_required
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

@login_required
def create_comment(request, id):
    new_comment = None
    post = JournalPost.objects.get(id=id)
    comments = Comment.objects.filter(post_title=post).order_by('-id')
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
            # return render(request, 'post_detail.html', {'post':post, 'comments':comments})
    else:
        form = CommentForm()
    return render(request, 'create_comment.html',
    { 'form': form })

@login_required
def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        content_search = JournalPost.objects.filter(content__icontains=searched, privacy=0).order_by('-created_at')
        return render(request, 'search.html', context={'searched':searched, 'content_search':content_search})
    else:
        return render(request, 'search.html', context={})

from django.views import generic

class UpdatePostView(UpdateView):
    model = JournalPost
    template_name = 'update_post.html'
    fields=['title','content', 'type', 'category', 'privacy', 'colors_seen']
    def get_success_url(self):
        return reverse('home')

class DeletePostView(DeleteView):
    model = JournalPost
    template_name = 'delete_post.html'
    fields=['title','content', 'type', 'category', 'privacy', 'colors_seen']
    def get_success_url(self):
        return reverse('home')

class PostListView(generic.ListView):
   queryset = JournalPost.objects.filter(privacy=0).order_by('-created_at')
   template_name = 'home.html'

class NightmareListView(generic.ListView):
    queryset = JournalPost.objects.filter(type='Nightmare', privacy=0).order_by('-created_at')
    template_name = 'nightmare.html'

class DreamListView(generic.ListView):
    queryset = JournalPost.objects.filter(type='Dream', privacy=0).order_by('-created_at')
    template_name = 'dream.html'

class RealityListView(generic.ListView):
    queryset = JournalPost.objects.filter(category='Reality', privacy=0).order_by('-created_at')
    template_name = 'reality.html'

class FantasyListView(generic.ListView):
    queryset = JournalPost.objects.filter(category='Fantasy/Unreal', privacy=0).order_by('-created_at')
    template_name = 'fantasy.html'


from django.views.generic import TemplateView

class AboutPageView(TemplateView):
    template_name = 'about.html'

# added for likes and dislikes button
class AddLike(LoginRequiredMixin, View):
  def post(self, request, pk, *args, **kwargs):
      post = JournalPost.objects.get(pk=pk)

      is_dislike = False

      for dislike in post.dislikes.all():
        if dislike == request.user:
          is_dislike = True
          break

      if is_dislike:
        post.dislikes.remove(request.user)

      is_like = False

      for like in post.likes.all():
        if like == request.user:
          is_like = True
          break

      if not is_like:
        post.likes.add(request.user)

      if is_like:
        post.likes.remove(request.user)

      next = request.POST.get('next', '/')
      return HttpResponseRedirect(next)

class AddDislike(LoginRequiredMixin, View):
  def post(self, request, pk, *args, **kwargs):
      post = JournalPost.objects.get(pk=pk)

      is_like = False

      for like in post.likes.all():
        if like == request.user:
          is_like = True
          break

      if is_like:
        post.likes.remove(request.user)

      is_dislike = False

      for dislike in post.dislikes.all():
        if dislike == request.user:
          is_dislike = True
          break

      if not is_dislike:
        post.dislikes.add(request.user)

      if is_dislike:
        post.dislikes.remove(request.user)

      next = request.POST.get('next', '/')
      return HttpResponseRedirect(next)
