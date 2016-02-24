from django.contrib import admin
from models import ActivateCode
class UserCernterAdmin(admin.ModelAdmin):
	list_display = ('owner', 'code')
admin.site.register(ActivateCode, UserCernterAdmin)
