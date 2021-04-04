"""Project3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('contact/shops/main/',views.mainshop, name='mainshop'),
    path('querydata/hsa/', views.querydata_hsa, name='querydata_hsa'), # Query data of HSA from XMMS

    path('search/<str:keyword>/<int:page>',views.search, name='search'), # Test path with parameter
    path('date/<int:year>-<int:month>-<int:day>/', views.date, name='date'), # Test path with parameter
    path('redirect/<path:url>', views.redirect, name='redirect'), # Test path with parameter
    path('article/<int:id>/<slug:title>/', views.show_article, name='show_article'), # Test path with parameter

    re_path('^drink/(?P<dnk>(coffee)|(tea)|(wine))/$', views.drink, name='drink'), # Use RegEx
    re_path(r'^title/(?P<title>[-\w\s]+)/$', views.show_title, name='show_title'), # Use RegEx with \Symbol
    re_path(r'^find/(?P<key>[\w\s]+)/(?P<page>\d+)/$', views.find, name='find'), # Use RegEx with \Symbol

    re_path(r'^testnoname/([\w\s]+)/(\d+)/$', views.test_no_name, name='test_no_name'), # Use RegEx with \Symbol แบบ ไม่กำหนด Name

    path('map/', views.maps)
]
