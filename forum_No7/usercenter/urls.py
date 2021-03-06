from django.conf.urls import url

urlpatterns = [
	url(r'^register/', 'usercenter.views.usercenter_register', name = 'usercenter_register'),
	url(r'^login/', 'usercenter.views.usercenter_login', name = 'usercenter_login'),
	url(r'^logout/', 'django.contrib.auth.views.logout_then_login', name='usercenter_logout'),
	url(r'^activate/(?P<activate_code>\w+)', 'usercenter.views.usercenter_activate', name = 'usercenter_activate'),
	url(r'^uploadavatar/', "usercenter.views.usercenter_upload_avatar", name="usercenter_upload_avatar"),
]
