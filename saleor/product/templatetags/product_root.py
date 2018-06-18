from django.template import Library, loader, Context
from django.utils.http import urlencode

from ..models import Category

register = Library()

# sækjum heimilistækjaflokkinn
@register.simple_tag()
def gulla_get_root(flokkur):
    gullaroot = Category.objects.get(name=flokkur)
    return gullaroot
