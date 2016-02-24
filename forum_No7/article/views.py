# -*-coding:utf-8-*-
from django.shortcuts import render, render_to_response, redirect
from models import Article
from block.models import Block
from django.template import RequestContext
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from utils import paginator as pa
from comment.models import Comment
from usercenter.models import UserProfile

def article_list(request, block_id):
	block_id = int(block_id)
	block = Block.objects.get(id = block_id)
	if request.GET.has_key('page_no'):
		page_no = int(request.GET['page_no'])
	else:
		page_no = 1
	block = Block.objects.get(id = block_id)
	articles = Article.objects.filter(block = block).order_by('-last_update_timestamp')

	articles, paginations = pa.paginator_query(articles, page_no)
	context = {"articles": articles, "b": block, "paginations": paginations}
	return render_to_response("article_list.html", context, context_instance=RequestContext(request))


@login_required
def article_create(request, block_id):
	block_id = int(block_id)
	block = Block.objects.get(id = block_id)
	if request.method == 'GET':
		return render_to_response('article_create.html', {'b': block}, context_instance = RequestContext(request))
	else:
		title = request.POST["title"].strip()
		content = request.POST["content"].strip()
		if not title or not content:
			messages.add_message(request, messages.ERROR, u'标题和内容不能为空')
			return render_to_response('article_create.html', {'b': block, 'title': title, 'content': content}, context_instance = RequestContext(request))
		author = request.user
		article = Article(title=title, content=content, author=author, block=block)
		article.save()
		# messages.add_message(request, messages.SUCCESS, u'成功发表文章')
		return redirect(reverse('article_list', args=[block.id]))

@login_required		
def article_display(request,article_id):
    article_id = int(article_id)
    article = Article.objects.get(id = article_id)
    if request.GET.has_key("comment_no"):
        comment_no = int(request.GET["comment_no"])
        profile = UserProfile.objects.get_or_create(owner=request.user)[0]
    else:
        comment_no = 1
        profile = None

    comments = Comment.objects.filter(article=article)
    comments, paginations = pa.paginator_query(comments, comment_no, displays=30, half_show_length=5)
    return render_to_response('article_display.html', {'article': article, 'comments': comments, 'paginations': paginations, 'profile': profile},           context_instance = RequestContext(request))
