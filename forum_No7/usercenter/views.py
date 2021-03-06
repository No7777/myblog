# -*- coding:utf-8 -*-
from django.contrib import messages
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from models import ActivateCode, UserProfile
from django.contrib.auth.views import login
import uuid, datetime
from django.contrib.auth.decorators import login_required
import os
from myforum import settings

def usercenter_register(request):
    error = ""
    if request.method == 'GET':
        return render_to_response('usercenter_register.html', {}, context_instance=RequestContext(request))
    else:
        username = request.POST['username'].strip()
        email = request.POST['email'].strip()
        password = request.POST['password'].strip()
        confirmed_pwd = request.POST['confirmed_pwd'].strip()
        if not username or not email or not password:
            error = u'所有信息都不能空!'
            messages.add_message(request, messages.WARNING, error)
            return render_to_response('usercenter_register.html', {}, context_instance = RequestContext(request))
        if password != confirmed_pwd:
            error = u'密码两次输入不一致!'
        if User.objects.filter(username=username).count() > 0:
            error = u'用户以存在!'
        if User.objects.filter(email=email).count() > 0:
            error = u'该邮箱已被注册!'
        if error:
            messages.add_message(request, messages.WARNING, error)
            return render_to_response('usercenter_register.html', {}, context_instance = RequestContext(request))
        else:
            new_code = str(uuid.uuid4()).replace('-', '')
            expire_time = datetime.datetime.now() + datetime.timedelta(days=2)
            activate_link = 'http://%s%s' % (request.get_host(), reverse('usercenter_activate', args=[new_code]))
            try:
                send_mail(u'我的论坛', u'欢迎注册,请使用如下地址激活账号 %s:%s' % (username, activate_link), 'xqflame@sina.com', [email], fail_silently=False)
            except Exception as e:
                print e
                messages.add_message(request, messages.WARNING, u'邮件发送失败！')
                return render_to_response('usercenter_register.html', {}, context_instance = RequestContext(request))
            messages.add_message(request, messages.INFO, u'邮件已发送，请激活！')
            user = User.objects.create_user(username=username, email=email, password=password)
            user.is_active = False
            user.save()
            code_record = ActivateCode(owner=user, code=new_code, expire_timestamp=expire_time)
            code_record.save()
            print activate_link
            return render_to_response('usercenter_register.html', {}, context_instance=RequestContext(request))
            
def usercenter_login(request):
    next_lnk = ''
    if request.GET.has_key('next'):
        next_lnk = request.GET['next']
    if request.method == 'GET':
        return render_to_response('usercenter_login.html', {'next': next_lnk}, context_instance=RequestContext(request))
    else:
        username = request.POST['username'].strip()
        password = request.POST['password'].strip()
        next_lnk = request.POST['next'].strip()
        
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                print next_lnk
                if next_lnk:
                    return redirect(next_lnk)
                else:
                    return redirect(reverse('block_list'))
            else:
                messages.add_message(request, messages.WARNING, u'用户没有激活！')
        else:
            messages.add_message(request, messages.WARNING, u'用户名密码错误！')
        return render_to_response('usercenter_login.html', {'next': next_lnk}, context_instance=RequestContext(request))


def usercenter_activate(request, activate_code):
    code_set = ActivateCode.objects.filter(code=activate_code, expire_timestamp__gt=datetime.datetime.now())
    if code_set.count() == 1:
        user = code_set[0].owner
        user.is_active = True
        user.save()
        messages.add_message(request, messages.WARNING, u'该账户已成功激活，请登录！')
        return render_to_response('usercenter_login.html', {}, context_instance = RequestContext(request))
    else:
        error = ""
        code_set = ActivateCode.objects.filter(code=activate_code)
        if code_set.count() >= 1:
            error = u'该账户没有成功注册或激活码已过期,请重新注册！'
            user = code_set[0].owner
            code_set.selete()
            user.delete()
        else:
            error = u'该账户没有成功注册，请重新注册！'
            
        messages.add_message(request, messages.WARNING, error)
        return render_to_response('usercenter_register', {}, context_instance = RequestContext(request))
		
		
@login_required
def usercenter_upload_avatar(request):
    if request.method == "GET":
        return render_to_response("usercenter_upload_avatar.html", {}, context_instance=RequestContext(request))
    else:
        avatar_file = request.FILES.get("avatar", None)
        if not avatar_file:
            messages.add_message(request, messages.WARNING, u"没有选择上传文件！")
            return render_to_response("usercenter_upload_avatar.html", {}, context_instance=RequestContext(request))
        file_name = request.user.username + "_" + avatar_file.name
        file_path = os.path.join(settings.STORAGE_PATH, file_name)

        with open(file_path, 'wb+') as target:
            for chunk in avatar_file.chunks():
                target.write(chunk)
                
        url = "%s/avatar/%s" % (settings.USER_RES_URL_BASE, file_name)
        profile = UserProfile.objects.get(owner=request.user)
        profile.avatar = url
        profile.save()
        
        return redirect(reverse("block_list"))
