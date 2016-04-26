# coding: utf-8

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