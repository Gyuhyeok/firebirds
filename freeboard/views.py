from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context
from freeboard.models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def board(request): #post_list
	template = get_template('board.html')

	page_data = Paginator(Post.objects.all(), 5)
	page = request.GET.get('page')
	if page is None:
		page = 1
	try:
		posts = page_data.page(page)
	except PageNotAnInteger:
		posts = page_data.page(1)
	except EmptyPage:
		posts = page_data.page(page_data.num_pages)

	context = Context({'board': posts, 'current_page':int(page), 'total_page':range(1, page_data.num_pages + 1)})

	return HttpResponse(template.render(context))

# Create your views here.
