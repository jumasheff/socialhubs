# coding: utf-8
from decimal import Decimal
from django.shortcuts import render

from apps.social_objects.models import Category, SocialHub


def home(request):
    context = {}
    context['title'] = u'Главная'
    categories = Category.objects.all()
    socials = SocialHub.objects.all()
    if 'category' in request.GET and request.GET['category']:
        category = request.GET.get('category', '')
        socials = socials.filter(category=category)
    context['categories'] = categories
    context['socials'] = socials
    return render(request, 'main.html', context)


def search_road_map(request):
    context = {}
    context['title'] = u'Расчет маршрута'
    radius = 1
    lat = Decimal(request.GET.get('lat', '42.780486'))
    lng = Decimal(request.GET.get('lng', '74.667276'))
    km_lat = Decimal('0.008968609865')
    km_lng = Decimal('0.01492537313')
    end_lat = lat + (radius * km_lat)
    end_lng = lng - (radius * km_lat)
    categories = Category.objects.all()
    socials = SocialHub.objects.all()
    if 'category' in request.GET and request.GET['category']:
        category = request.GET.get('category', '')
        socials = socials.filter(category=category)
    context['categories'] = categories
    context['socials'] = socials
    context['lat'] = lat
    context['lng'] = lng
    context['end_lat'] = end_lat
    context['end_lng'] = end_lng
    return render(request, 'search_road_map.html', context)
