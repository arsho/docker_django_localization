from django.shortcuts import render

from .models import News

def index(request):
    news_list = News.objects.all()
    data = {'news_list': news_list}
    return render(request, 'news/index.html', data)

def about(request):
    data = {
        'site_name': "Newspaper Site",
        'author': 'Some Publisher'
    }
    return render(request, 'news/about.html', data)
