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
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'


class SocialHub(models.Model):
    category = models.ForeignKey(Category, verbose_name=u'Категория', related_name='ctaegory_objects')

    cover = models.ImageField(u'Обложка', upload_to='social-hub/cover/')
    title = models.CharField(u'Название', max_length=500)
    description = models.TextField(u'Описание')

    address = models.CharField(u'Адрес', max_length=300, blank=True, null=True)
    phone = models.CharField(u'Телефон', max_length=50)
    email = models.EmailField(u'E-mail', blank=True, null=True)
    www = models.CharField(u'www', max_length=256, blank=True, null=True)

    bank = models.CharField(u'Банк', max_length=256, blank=True, null=True)
    special_account = models.CharField(u'Спец. счет', max_length=256, blank=True, null=True)
    personal_account = models.CharField(u'Лицевой счет', max_length=256, blank=True, null=True)

    latitude = models.DecimalField(u'Широта', max_digits=20, decimal_places=17)
    longitude = models.DecimalField(u'Долгота', max_digits=20, decimal_places=17)

    def __unicode__(self):
        return self.title

    def get_latitude(self):
        return '%s' % self.latitude

    def get_longitude(self):
        return '%s' % self.longitude

    @models.permalink
    def social_url(self):
        return ('social_item', (), {'slug': self.category.slug, 'id': self.id})

    class Meta:
        verbose_name = 'Социальный центр'
        verbose_name_plural = u'Социальные центры'


class ImageSocialHub(models.Model):
    social_hub = models.ForeignKey(SocialHub, verbose_name=u'', related_name='images')
    title = models.CharField(u'Название', max_length=256)
    image = models.ImageField(u'Картинка', upload_to='social-hub/image')
