# coding: utf-8
from django.shortcuts import render

from .models import Category, SocialHub


def category(request, slug):
    context = {}
    context['title'] = Category.objects.get(slug=slug).title
    context['category'] = Category.objects.get(slug=slug)
    return render(request, 'category.html', context)


def social_item(request, slug, id):
    context = {}
    context['title'] = SocialHub.objects.get(id=id).title
    category = Category.objects.get(slug=slug)
    context['social'] = SocialHub.objects.get(category=category, id=id)
    return render(request, 'social.html', context)
