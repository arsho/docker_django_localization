"""localization_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
js_info_dict = {
    'packages': ('news',),
}


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^news/', include('news.urls', namespace = 'news')),
    url(r'^jsi8n/$', 'django.views.i18n.javascript_catalog', js_info_dict),
]
