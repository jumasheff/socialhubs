from .models import Category, SocialObject


def categories(request):
	context = {}
	context['categories'] = Category.objects.all()
	return context


def socials(request):
	context = {}
	context['socials'] = SocialObject.objects.all()
	return context