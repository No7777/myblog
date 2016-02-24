# -*-coding:utf-8-*-
from django.db import models
from django.contrib.auth.models import User
class Block(models.Model):
	name = models.CharField(u"名字", max_length = 50)
	desc = models.CharField(u"描述", max_length = 100)
	manager = models.ForeignKey(User, verbose_name = u"管理员")

	create_timestamp = models.DateTimeField(u"创建时间", auto_now_add = True)
	last_update_timestamp = models.DateTimeField(u"最后更改时间", auto_now = True)

	def __unicode__(self):
		return self.name
	
	class Meta:
		verbose_name = u"板块"
		verbose_name_plural = u"板块"
