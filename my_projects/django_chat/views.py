from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Message

@login_required
def chat_view(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'chat/chat.html', {'users': users})
