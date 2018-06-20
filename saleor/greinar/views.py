import datetime

from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse

from .utils import greinars_visible_to_user


def greinar_details(request, slug):
    greinar = get_object_or_404(
        greinars_visible_to_user(user=request.user).filter(slug=slug))
    #today = datetime.date.today()
    is_visible = ()
        #greinar.available_on is None or greinar.available_on <= today)
    return TemplateResponse(
        request, 'greinar/details.html', {
            'greinar': greinar})
