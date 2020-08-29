from django.urls import path
from .views import index_view, ToDoListView, ToDoDetailView

app_name = 'todo'

urlpatterns = [
    path('', index_view),
    path('api/', ToDoListView.as_view()),
    path('api/<int:pk>/', ToDoDetailView.as_view()),
]
