# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
class ActivateCode(models.Model):
    owner = models.ForeignKey(User, verbose_name = u"用户")
    code = models.CharField(u"激活码", max_length = 250)
    expire_timestamp = models.DateTimeField()
    
    create_timestamp = models.DateTimeField(auto_now_add=True)
    last_update_timstamp = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.code
        
    class Meta:
        verbose_name = u"激活码"
        verbose_name_plural = u"激活码"
        
class UserProfile(models.Model):
    owner = models.ForeignKey(User, verbose_name=u"用户")
    avatar = models.CharField(u"头像", max_length=300, blank=True)

	
