from django.views.generic import View
from django.http import HttpResponse


class SummaryView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("foo")
