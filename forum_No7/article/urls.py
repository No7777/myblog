from django.conf.urls import url

urlpatterns = [
	url(r'^lists/(?P<block_id>\d+)', 'article.views.article_list', name = 'article_list'),
	url(r'^create/(?P<block_id>\d+)', 'article.views.article_create', name = 'article_create'),
	url(r'^display/(?P<article_id>\d+)', 'article.views.article_display', name = 'article_display'),
]
