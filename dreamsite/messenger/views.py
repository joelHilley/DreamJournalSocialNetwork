from django.shortcuts import render, redirect
from messenger.models import Conversation, Message
from django.db.models import Q
from . import views
from django.views import generic, View
from .forms import ConversationForm, MessageForm
from account.models import Account
from django.contrib.auth.models import User


class ListConversations(View):
    def get(self, request, *args, **kwargs):
        conversations = Conversation.objects.filter(Q(user = request.user) | Q(reciever = request.user))

        context = {'conversations':conversations}

        return render(request, 'inbox.html', context)

class CreateConversation(View):
    def get(self, request, *args, **kwargs):
        form = ConversationForm()
        context = {'form':form}

        return render(request, 'new_convo.html', context)

    def post(self, request, *args, **kwargs):
        form = ConversationForm(request.POST)

        username = request.POST.get('username')

        try:
            reciever = Account.objects.get(username=username)
            if Conversation.objects.filter(user=request.user, reciever=reciever).exists():
                conversation = Conversation.objects.filter(user=request.user, reciever=reciever)[0]
                return redirect('conversation', pk=conversation.pk)
            elif Conversation.objects.filter(user=reciever, reciver=request.user).exists():
                conversation = Conversation.objects.filter(user=reciever, reciver=request.user)[0]
                return redirect('conversation', pk=conversation.pk)

            if form.is_valid():
                conversation = Conversation(user=request.user, reciever=reciever)
                conversation.save()

                return redirect('conversation', pk=conversation.pk)
        except:
            return redirect('new_convo')

class ConversationView(View):
    def get(self, request, pk, *args, **kwargs):
        form = MessageForm()
        conversation = Conversation.objects.get(pk=pk)
        message_list = Message.objects.filter(conversation__pk__contains=pk)

        context = {'form':form,'conversation':conversation,'message_list':message_list}

        return render(request, 'convo.html', request)




# class InboxListView(generic.ListView):
#    queryset = Conversation.objects.order_by('-created_on')
#    template_name = 'inbox.html'

# class MessageDetailView(generic.DetailView):
#     model = JournalPost
#     template_name = 'post_detail.html'
