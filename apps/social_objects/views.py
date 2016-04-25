# coding: utf-8
from django.shortcuts import render

from .models import Category


def category(request, slug):
	context = {}
	context['title'] = Category.objects.get(slug=slug)
	context['category'] = Category.objects.get(slug=slug)
	return render(request, 'category.html', context)