from django.conf.urls import include, url

urlpatterns = [
    url(r'^create/', 'comment.views.comment_create', name='comment_create'),
    #url(r'^list/', 'comment.views.comment_list', name='comment_list'),
]

