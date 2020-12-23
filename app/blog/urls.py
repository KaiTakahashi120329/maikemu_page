from django.urls import path
from .views import BlogFunc, CategoryFunc, ListFunc, DetailFunc, ContactView, ContentView, SendEmailView, SuccessFunc, privacyView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', BlogFunc, name='top'),
    path('category/<str:category>', CategoryFunc, name='category'),
    path('list/', ListFunc, name='list'),
    path('detail/<int:pk>/', DetailFunc, name='detail'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('contact/content/', ContentView.as_view(), name='content'),
    path('contact/send_email/', SendEmailView.as_view(), name='send'),
    path('contact/success/', SuccessFunc, name='success'),
    path('privacy/', privacyView.as_view(), name='privacy'),
]
