# coding: utf-8

from django.db import models


class Category(models.Model):
	title = models.CharField(u'Заголовок', max_length=256)
	slug = models.SlugField(u'Ярлык', blank=True, null=True)
	point = models.FileField(u'Маркер', upload_to='social/point')

	def __unicode__(self):
		return self.title

	@models.permalink
	def get_category(self):
		return ('category', (), {'slug': self.slug})

	class Meta:
		verbose_name=u'Категория'
		verbose_name_plural=u'Категории'


class SocialObject(models.Model):
	category = models.ForeignKey(Category, verbose_name=u'Категория', related_name='ctaegory_objects')

	cover = models.ImageField(u'Обложка', upload_to='social/objects/cover/')
	title = models.CharField(u'Название', max_length=500)
	description = models.TextField(u'Описание')

	phone = models.CharField(u'Телефон', max_length=50)

	email = models.EmailField(u'E-mail')

	latitude = models.DecimalField(u'Широта', max_digits=20, decimal_places=17)
	longitude = models.DecimalField(u'Долгота', max_digits=20, decimal_places=17)

	def get_latitude(self):
		return '%s' % self.latitude

	def get_longitude(self):
		return '%s' % self.longitude

	def __unicode__(self):
		return self.title

