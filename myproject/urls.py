"""myproject URL Configuration

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
from django.urls import path
from mydiary import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('new/', views.new, name="new"),
    path('detail/<int:index>', views.detail, name="detail"),
    path('edit/<int:index>', views.edit, name='edit'),
    path('detail/<int:pk>/delete', views.delete, name="delete"),
    #view에서 함수를 만들어준 후 꼭 path 적어줘야 한다
    path('detail/<int:index>/comment/<int:comment_pk>/delete', views.delete_comment, name="delete_comment"),
]

