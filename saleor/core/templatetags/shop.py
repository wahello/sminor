from django.template import Library, loader, Context
from django.utils.http import urlencode

from ..context_processors import NAVIGATION_CONTEXT_NAME

from ...product.models import Category

register = Library()


@register.simple_tag(takes_context=True)
def get_sort_by_url(context, field, descending=False):
    request = context['request']
    request_get = request.GET.dict()
    if descending:
        request_get['sort_by'] = '-' + field
    else:
        request_get['sort_by'] = field
    return '%s?%s' % (request.path, urlencode(request_get))

@register.simple_tag(takes_context=True)
def menu(context, template_name, site_menu=None, horizontal=False):
    if not site_menu:
        return
    menus = context[NAVIGATION_CONTEXT_NAME]
    menu = next((menu for menu in menus if menu.pk == site_menu.pk), None)
    if not menu:
        return
    menu_items = [item for item in menu.items.all() if item.parent_id is None]
    heim = Category.objects.get(name="Heimilistæki")
    raf = Category.objects.get(name="Söludeild rafbúnaðar")
    t = loader.get_template(template_name)
    return t.render({
        'menu_items': menu_items,
        'horizontal': horizontal,
        'catMenuHeim': heim,
        'rafMenuHeim': raf
        })
