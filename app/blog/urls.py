from django.urls import path
from .views import BlogFunc, CategoryFunc, ListFunc, DetailFunc

urlpatterns = [
    path('', BlogFunc, name='top'),
    path('category/<str:category>', CategoryFunc, name='category'),
    path('list/', ListFunc, name='list'),
    path('detail/<int:pk>/', DetailFunc, name='detail'),
]
