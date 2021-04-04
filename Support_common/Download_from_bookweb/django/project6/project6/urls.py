"""project6 URL Configuration

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
    path('', views.index),
    path('request-obj/', views.request_obj),
    path('form-get/', views.form_get),
    path('form-post/', views.form_post),

    path('search/', views.search),
    path('product/', views.product),
    path('field-args/', views.field_args),
    path('form-as-table/', views.as_table),
    path('form-as-p/', views.as_p),
    path('form-crispy/', views.crispy)

]