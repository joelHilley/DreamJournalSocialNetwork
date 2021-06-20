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
    #return render(request, 'post_detail.html', {'post': post})
    #comments
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = comment
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'post_detail.html', {'comment':comment,
                                                    'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

#view profile of  users
def user_detail(request, pk):
    profile = Account.objects.get(pk=pk)
    return render(request, 'user_detail.html', {'pk':pk, 'profile':profile})

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

from django.views import generic

class PostListView(generic.ListView):
   queryset = JournalPost.objects.filter(privacy=0).order_by('-created_at')
   template_name = 'home.html'

class PostDetailView(generic.DetailView):
    model = JournalPost
    template_name = 'post_detail.html'

# class UserDetailView(generic.DetailView):
#     model = JournalPost
#     #pk_url_kwarg = 'username_id' #changes url requirement from primary key to  username_id
#     template_name = 'user_detail.html'

from django.views.generic import TemplateView

class AboutPageView(TemplateView):
    template_name = 'about.html'
