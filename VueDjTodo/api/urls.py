from unicodedata import name
from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
  path('todo/list/', views.ApiTodoLV.as_view(), name='list'),
  path('todo/<int:pk>/delete/', views.ApiTodoDelV.as_view(), name='delete'),
]
