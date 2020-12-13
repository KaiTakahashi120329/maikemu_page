from django.urls import path
from .views import BlogFunc, CategoryFunc

urlpatterns = [
    path('', BlogFunc, name='top'),
    path('category/<str:category>', CategoryFunc, name='category'),
]
