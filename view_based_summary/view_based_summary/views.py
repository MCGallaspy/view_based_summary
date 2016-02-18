from django.db.models.signals import post_save
from django.dispatch import receiver
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


@receiver(post_save, sender=ContentInteractionLog)
def invalidate_cache(*args, **kwargs):
    """
        Depending on the cache used, we could implement more granular cache invalidation.
        This signal can also inspect the instance being saved in the kwargs:
        https://docs.djangoproject.com/en/1.9/ref/signals/#post-save
    """
    summary_view_helper.cache_clear()
