"""project4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('products/detail/', views.product_detail, name='pro_detail'),

    path('variable/', views.variable),
    path('tag/if/', views.tag_if),
    path('tag/for/', views.tag_for),
    path('tag/auto-escape/', views.tag_auto_escape),
    path('tag/others/', views.tag_others),

    path('', views.home, name='index'),

    path('filter/str-list-num/', views.filter_str_list_num),
    path('filter/num/', views.filter_num),
    path('filter/string/', views.filter_string),
    path('filter/special-chars/', views.filter_special_chars),
    path('filter/url/', views.filter_url),
    path('filter/datetime/', views.filter_datetime),
    path('filter/custom/', views.filter_custom),

    path('redirect/from/', views.redirect_from, name='redirect_from'),
    path('redirect/to/', views.redirect_to, name='redirect_to'),
    path('redirect/error/<int:code>/<str:text>/', views.redirect_error, name='redirect_error'),

    path('main/', views.main),
    path('home/', views.home),
    path('products/', views.products),   
]

