"""hora URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from app import views
from django.views.generic import TemplateView
from app.views import EnlaceListView, EnlaceDetailView, EnlaceViewSet, UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'links',EnlaceViewSet)
router.register(r'users',UserViewSet)

urlpatterns = [    
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'app.views.home', name='home'),
    url(r'^plus/(\d+)$', 'app.views.plus', name='plus'),
    url(r'^minus/(\d+)$', 'app.views.minus', name='minus'),
    url(r'^categoria/(\d+)$', 'app.views.categoria', name='categoria'),
    url(r'^add/$', 'app.views.add', name='add'),

    url(r'^about/$', TemplateView.as_view(template_name='index.html'), name='about'),
    url(r'^enlaces/$', EnlaceListView.as_view(), name='enlaces'),
    url(r'^detalles/(?P<pk>[\d]+)$', EnlaceDetailView.as_view(), name='detalles'),


]
