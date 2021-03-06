# -*- coding:utf-8 -*-
from django.shortcuts import render, render_to_response
from models import Block
from django.template import RequestContext
from message.models import UserMessage
from usercenter.models import UserProfile
import logging

LOGGER = logging.getLogger('forum_No7')

def block_list(request):
    #LOGGER.info('Hello')
    if request.user.is_authenticated():
        msg_cnt = UserMessage.objects.filter(owner=request.user, status=0).count()
        profile = UserProfile.objects.get_or_create(owner=request.user)[0]
    else:
        msg_cnt = 0
        profile = None
    blocks = Block.objects.all().order_by('-id')
    return render_to_response('block_list.html', {'blocks': blocks, 'msg_cnt': msg_cnt, 'profile': profile}, context_instance=RequestContext(request)) 
