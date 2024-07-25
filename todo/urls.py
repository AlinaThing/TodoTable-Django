from django.urls import path
from .views import TodoLists, success, EditTodoItem, DeleteTodoItem

urlpatterns = [
    path('', TodoLists, name='todolist'),
    path('success/', success, name='success'),
    path('edit/<int:pk>/', EditTodoItem, name='edit_todo_item'),
    path('delete/<int:pk>/', DeleteTodoItem, name='delete_todo_item'),
]
