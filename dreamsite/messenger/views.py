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
        conversations = Conversation.objects.filter(Q(user = request.user) | Q(receiver = request.user))

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
            receiver = Account.objects.get(username=username)
            if Conversation.objects.filter(user=request.user, receiver=receiver).exists():
                conversation = Conversation.objects.filter(user=request.user, receiver=receiver)[0]
                return redirect('conversation', pk=conversation.pk)
            elif Conversation.objects.filter(user=receiver, receiver=request.user).exists():
                conversation = Conversation.objects.filter(user=receiver, receiver=request.user)[0]
                return redirect('conversation', pk=conversation.pk)

            if form.is_valid():
                conversation = Conversation(user=request.user, receiver=receiver)
                conversation.save()

                return redirect('conversation', pk=conversation.pk)
        except:
            return redirect('inbox')

class ConversationView(View):
    def get(self, request, pk, *args, **kwargs):
        form = MessageForm()
        convo = Conversation.objects.get(pk=pk)
        message_list = Message.objects.filter(convo__pk__contains=pk)

        context = {'form':form,'convo':convo,'message_list':message_list}

        return render(request, 'convo.html', context)

class NewMessage(View):
    def post(self, request, pk, *args, **kwargs):
        conversation = Conversation.objects.get(pk=pk)
        if conversation.receiver == request.user:
            receiver = conversation.user
        else:
            receiver = conversation.receiver

        message = Message(
            convo=conversation,
            sender=request.user,
            recipient=receiver,
            message=request.POST.get('message')
        )

        message.save()
        return redirect('convo', pk=pk)



# class InboxListView(generic.ListView):
#    queryset = Conversation.objects.order_by('-created_on')
#    template_name = 'inbox.html'

# class MessageDetailView(generic.DetailView):
#     model = JournalPost
#     template_name = 'post_detail.html'
