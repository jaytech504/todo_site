"""
URL configuration for todo_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from todo import views as todo_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todo_views.index, name='todo'),
    path('post/new/', todo_views.PostCreateView.as_view(), name='post-create'),
    path('todo/<int:pk>/update/', todo_views.PostUpdateView.as_view() , name = 'edit'),
    path('todo/<int:pk>/delete', todo_views.PostDeleteView.as_view(), name="del"),
    path('favorite', todo_views.favorites, name='fav'),
]
