"""project11 URL Configuration

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

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('cookie/test/', views.cookie_test, name="cookie_test"),
    path('cookie/test/result/', views.cookie_test_result, name='cookie_test_result'),

    path('cookie/signin/', views.cookie_signin),

    path('session/captcha/', views.session_captcha),

    path('session/signin/', views.session_signin, name='signin'),
    path('session/signout/', views.session_signout, name='signout'),

    path('session/rv/', views.session_rv_index, name='rv_index'),
    path('session/rv/html/', views.session_rv_html, name='rv_html'),
    path('session/rv/css/', views.session_rv_css, name='rv_css'),
    path('session/rv/js/', views.session_rv_js, name='rv_js'),
    path('session/rv/bs/', views.session_rv_bs, name='rv_bs'),
    path('session/rv/django/', views.session_rv_django, name='rv_django'),
]


