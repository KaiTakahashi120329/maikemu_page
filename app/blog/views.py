from django.shortcuts import render, get_object_or_404, redirect
from .models import BaseModel, Category
import datetime

def CategoryFunc(request, category):
    category = Category.objects.get(name=category)
    object_list = BaseModel.objects.all().filter(category=category)
    return render(request, 'category.html', { 'category':category, 'object_list':object_list})

def BlogFunc(request):
    object_list = BaseModel.objects.all()
    return render(request, 'top.html',  {'object_list':object_list})