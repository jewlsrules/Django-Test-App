"""clients URL Configuration

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
from .views import list_clients, test_function, special_case_2003, special_case, month_archive, hello

urlpatterns = [
    path('hello/<str:name>/', hello),
    path('articles/2003/', special_case_2003),
    path('articles/<int:year>/', special_case),
    path('articles/<int:year>/<int:month>/', month_archive),
    path('test/', test_function),
    path('clients/', list_clients),
    path('admin/', admin.site.urls),
]
