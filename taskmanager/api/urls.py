from django.urls import path
from .views import (
    UserListCreateView,
    UserRetrieveUpdateDestroyView,
    TaskListView,
    TaskCreateView,
    TaskRetrieveView,
    TaskUpdateView,
    TaskDestroyView,
)

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/', TaskRetrieveView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', TaskDestroyView.as_view(), name='task-delete'),

]
