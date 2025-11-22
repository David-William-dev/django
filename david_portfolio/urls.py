"""
URL configuration for david_portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from test_django import views

handler404 = 'david_portfolio.views.custom_404'

urlpatterns = [
    path("test/",include("test_django.urls")),
    path("",view=views.redirectUrl,name="redirect_home"),
    # path("home/",urls.index,name="fine"),
    # path("fine/",urls.getFine,name="fineornot"),
    # path("post/<id>/",urls.dynamicUrl,name="dynamo"),
    path("admin/", admin.site.urls),
]
