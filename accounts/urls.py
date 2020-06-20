# myblog/accounts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.sighup.as_view(), name='signup')
]
