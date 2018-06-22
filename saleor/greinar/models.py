import datetime

from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.utils.translation import pgettext_lazy

from ..core.utils import build_absolute_uri
from ..seo.models import SeoModel

from mptt.models import MPTTModel

from django.utils.text import slugify

from ckeditor_uploader.fields import RichTextUploadingField


class greinarQuerySet(models.QuerySet):
    def public(self):
        #today = datetime.date.today()
        return self
            #Q(is_visible=True), Q(available_on__lte=today) | Q(available_on__isnull=True)



class greinar(SeoModel):
    slug = models.SlugField(max_length=100, null=True, blank=True)
    title = models.CharField(unique=True, max_length=200)
    titletext = models.CharField(max_length=200)
    content = RichTextUploadingField()

    image = models.ImageField(upload_to='greinamyndir/%Y/%m/', blank=True, null=True)

    SIZE_CHOICES = (
        ('lítil', 'Lítil'),
        ('stór', 'Stór'),
    )

    image_size = models.CharField(choices=SIZE_CHOICES, default='lítil', max_length=20)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    objects = greinarQuerySet.as_manager()

    class Meta:
        ordering = ('slug',)
        permissions = (
            ('view_greinar',
             pgettext_lazy('Permission description', 'Can view greinars')),
            ('edit_greinar',
             pgettext_lazy('Permission description', 'Can edit greinars')))

    def __str__(self):
        return self.title

# býr til slug útfrá titlinum
##########################################
    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while greinar.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)
##########################################

    def get_absolute_url(self):
        return reverse('greinar:details', kwargs={'slug': self.slug})

    def get_full_url(self):
        return build_absolute_uri(self.get_absolute_url())
