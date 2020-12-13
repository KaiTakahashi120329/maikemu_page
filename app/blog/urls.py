from django.urls import path
from .views import BlogFunc, CategoryFunc, ListFunc

urlpatterns = [
    path('', BlogFunc, name='top'),
    path('category/<str:category>', CategoryFunc, name='category'),
    path('list/', ListFunc, name='list'),
]
