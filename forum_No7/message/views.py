from django.shortcuts import render_to_response, redirect, RequestContext
from django.contrib.auth.decorators import login_required
from message.models import UserMessage


@login_required
def message_list(request):
    read_messages = UserMessage.objects.filter(owner=request.user, status=1).order_by("-id")
    unread_messages = UserMessage.objects.filter(owner=request.user, status=0).order_by("-id")

    return render_to_response("message_list.html",
                              {"read_messages": read_messages, "unread_messages": unread_messages},
                              context_instance=RequestContext(request))


@login_required
def message_read(request, message_id):
    msg = UserMessage.objects.get(id=int(message_id))
    msg.status = 1
    msg.save()
    return redirect(msg.link)

