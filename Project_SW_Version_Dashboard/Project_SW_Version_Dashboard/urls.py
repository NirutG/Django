"""Project_SW_Version_Dashboard URL Configuration

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

    # path('', views.index, name='index'),
    # path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
    # path('contact/shops/main/',views.mainshop, name='mainshop'),
    # path('querydata/hsa/', views.querydata_hsa, name='querydata_hsa'), # Query data of HSA from XMMS

    # path('search/<str:keyword>/<int:page>',views.search, name='search'), # Test path with parameter
    # path('date/<int:year>-<int:month>-<int:day>/', views.date, name='date'), # Test path with parameter
    # path('redirect/<path:url>', views.redirect, name='redirect'), # Test path with parameter
    # path('article/<int:id>/<slug:title>/', views.show_article, name='show_article'), # Test path with parameter

    # re_path('^drink/(?P<dnk>(coffee)|(tea)|(wine))/$', views.drink, name='drink'), # Use RegEx
    # re_path(r'^title/(?P<title>[-\w\s]+)/$', views.show_title, name='show_title'), # Use RegEx with \Symbol
    # re_path(r'^find/(?P<key>[\w\s]+)/(?P<page>\d+)/$', views.find, name='find'), # Use RegEx with \Symbol

    # re_path(r'^testnoname/([\w\s]+)/(\d+)/$', views.test_no_name, name='test_no_name'), # Use RegEx with \Symbol แบบ ไม่กำหนด Name

    # path('map/', views.maps),

    # For template
    path('', views.index, name='index'),
    path('detail/', views.sw_detail, name='detail'),
    path('test_variables/', views.test_variables, name='test_variables'),
    path('tag/if/', views.tag_if),
    path('tag/for/', views.tag_for),
    path('filter/str-list-num/', views.filter_str_list_num),
    path('filter/custom/', views.filter_custom),

    path('redirect/from/', views.redirect_from, name='redirect_from'),
    path('redirect/to/', views.redirect_to, name='redirect_to'),
    path('redirect/error/<int:code>/<str:text>/', views.redirect_error, name='redirect_error'),

    path('main/', views.main),
    path('main2/', views.main2),
    path('home/', views.home),
    path('products/', views.products),

    path('static-media/', views.static_media),
    path('static-css/', views.static_css),
    path('static-js/', views.static_js),
    path('static-bootstrap/', views.static_bootstrap),
    path('sw_dashboards/dashboard_0950/', views.dashboard_0950, name='dashboard_0950'),
    
    path('temp/', views.temp),


]
