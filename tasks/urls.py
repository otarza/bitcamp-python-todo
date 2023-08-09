from django.urls import path
from .views import TaskView, CategoryView
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'tasks', TaskView, 'task')
router.register(r'categories', CategoryView)

urlpatterns = [
    path('', include(router.urls)),
]
