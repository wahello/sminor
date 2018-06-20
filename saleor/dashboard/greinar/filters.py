from django.utils.translation import npgettext, pgettext_lazy
from django_filters import CharFilter, OrderingFilter

from ...core.filters import SortedFilterSet
from ...greinar.models import greinar

SORT_BY_FIELDS = {
    'title': pgettext_lazy('greinar list sorting option', 'title'),
    'url': pgettext_lazy('greinar list sorting option', 'url')}


class greinarFilter(SortedFilterSet):
    title = CharFilter(
        label=pgettext_lazy('greinar list title filter label', 'Title'),
        lookup_expr='icontains')
    url = CharFilter(
        label=pgettext_lazy('greinar list url filter label', 'URL'),
        lookup_expr='icontains')
    sort_by = OrderingFilter(
        label=pgettext_lazy('greinar list sorting filter label', 'Sort by'),
        fields=SORT_BY_FIELDS.keys(),
        field_labels=SORT_BY_FIELDS)

    class Meta:
        model = greinar
        fields = []

    def get_summary_message(self):
        counter = self.qs.count()
        return npgettext(
            'Number of matching records in the dashboard greinar list',
            'Found %(counter)d matching greinar',
            'Found %(counter)d matching greinars',
            number=counter) % {'counter': counter}
