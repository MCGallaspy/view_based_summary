from django.views.generic import View
from django.http import HttpResponse

from models import ContentInteractionLog


class SummaryView(View):
    def get(self, request, *args, **kwargs):
        user = kwargs['user']
        total = 0

        for cl in ContentInteractionLog.objects.filter(user=user):
            total += cl.completion_timestamp - cl.start_timestamp

        return HttpResponse(str(total))
