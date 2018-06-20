from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.utils.translation import pgettext_lazy

from ...core.utils import get_paginator_items
from ...greinar.models import greinar
from ..views import staff_member_required
from .filters import greinarFilter
from .forms import greinarForm


@staff_member_required
@permission_required('greinar.view_greinar')
def greinar_list(request):
    greinars = greinar.objects.all()
    greinars_filter = greinarFilter(request.GET, queryset=greinars)
    greinars = get_paginator_items(
        greinars_filter.qs, settings.DASHBOARD_PAGINATE_BY,
        request.GET.get('greinar'))
    ctx = {
        'greinars': greinars, 'filter_set': greinars_filter,
        'is_empty': not greinars_filter.queryset.exists()}
    return TemplateResponse(request, 'dashboard/greinar/list.html', ctx)


@staff_member_required
@permission_required('greinar.edit_greinar')
def greinar_update(request, pk):
    Greinar = get_object_or_404(greinar, pk=pk)
    return _greinar_edit(request, Greinar)


@staff_member_required
@permission_required('greinar.edit_greinar')
def greinar_add(request):
    Greinar = greinar()
    return _greinar_edit(request, Greinar)


def _greinar_edit(request, greinar):
    form = greinarForm(request.POST or None, instance=greinar)
    if form.is_valid():
        form.save()
        msg = pgettext_lazy('Dashboard message', 'Saved greinar')
        messages.success(request, msg)
        return redirect('dashboard:greinar-details', pk=greinar.pk)
    ctx = {
        'greinar': greinar, 'form': form}
    return TemplateResponse(request, 'dashboard/greinar/form.html', ctx)


@staff_member_required
@permission_required('greinar.edit_greinar')
def greinar_delete(request, pk):
    Greinar = get_object_or_404(greinar, pk=pk)
    if request.POST:
        greinar.delete()
        msg = pgettext_lazy(
            'Dashboard message', 'Removed greinar %s') % (greinar.title,)
        messages.success(request, msg)
        return redirect('dashboard:greinar-list')
    ctx = {'greinar': Greinar}
    return TemplateResponse(request, 'dashboard/greinar/modal_delete.html', ctx)


@staff_member_required
@permission_required('greinar.view_greinar')
def greinar_details(request, pk):
    Greinar = get_object_or_404(greinar, pk=pk)
    ctx = {'greinar': Greinar}
    return TemplateResponse(request, 'dashboard/greinar/detail.html', ctx)
