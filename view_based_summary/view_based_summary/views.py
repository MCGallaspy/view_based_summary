from django.views.generic import View
from django.http import HttpResponse

from models import ContentInteractionLog

from functools32 import lru_cache


class SummaryView(View):
    def get(self, request, *args, **kwargs):
        user = kwargs['user']
        total = summary_view_helper(user)
        return HttpResponse(str(total))


@lru_cache(maxsize=128)
def summary_view_helper(user):
    total = 0

    for cl in ContentInteractionLog.objects.filter(user=user):
        total += cl.completion_timestamp - cl.start_timestamp

    return total
