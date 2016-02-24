# -*-coding:utf-8-*-
from django.contrib.auth.decorators import login_required
from article.models import Article
from comment.models import Comment
from utils import response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import render_to_response
from message.models import UserMessage

@login_required
def comment_create(request):
    article_id = int(request.POST["article_id"])
    to_comment_id = int(request.POST["to_comment_id"])
    content = request.POST["content"]
    page_nums = request.POST["page_nums"]
    article = Article.objects.get(id=article_id)
    block = article.block
    owner = request.user
    

    comment = Comment(block=block, article=article, owner=owner, to_comment_id=to_comment_id, content=content)
    comment.save()

    if to_comment_id == 0:
        msg = UserMessage(owner=article.author,
                          content=u"有人评论了你的文章：《%s》" % article.title,
                          link=reverse("article_display", args=[article.id])+ "?comment_no=" + page_nums)
        msg.save()
    else:
        to_comment = Comment.objects.get(id=to_comment_id)
        msg = UserMessage(owner=to_comment.owner,
                          content=u"有人评论了你的评论：'%s'" % to_comment.content[:20],
                          link=reverse("article_display", args=[article.id]) + "?comment_no=" + page_nums)
        msg.save()

    return response.json_response({})


