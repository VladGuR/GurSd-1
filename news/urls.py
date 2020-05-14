from django.urls import re_path
import news.views as news

app_name = 'news'  # ОБЯЗАТЕЛЬНО!!!

urlpatterns = [
    re_path('', news.news, name='news'),
    re_path('^news/(?P<new>.*\s*)/$', news.new, name='new'),
]
