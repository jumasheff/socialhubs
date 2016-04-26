from .models import Category, SocialHub


def categories(request):
	context = {}
	context['categories'] = Category.objects.all()
	return context


def socials(request):
	context = {}
	context['socials'] = SocialHub.objects.all()
	return context