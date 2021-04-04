"""project9 URL Configuration

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
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('employee/create/', views.employee_create, name='emp_create'),
    path('employee/read/', views.employee_read),
    path('employee/search/', views.employee_search),
    path('employee/edit/', views.employee_edit, name='emp_edit'),
    path('employee/update/<int:id>/', views.employee_update, name='emp_update'),
    path('employee/delete/<int:id>/', views.employee_delete, name='emp_delete'),

    path('member/signin/', views.member_signin),

    re_path(r'pagination/prev-next/(?P<pg>\d*/?)', views.pagination_pvnx, name='pg_pvnx'),
    re_path(r'pagination/page-num/(?P<pg>\d*/?)', views.pagination_num, name='pg_num'),
    re_path(r'pagination/bootstrap/(?P<pg>\d*/?)', views.pagination_bs, name='pg_bs'),
]
