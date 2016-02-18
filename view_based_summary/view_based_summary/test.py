from django.test import TestCase
from django.core.urlresolvers import reverse

from models import ContentInteractionLog


class SummaryViewTestCase(TestCase):

    def setUp(self):
        ContentInteractionLog.objects.create(
            user=1,
            start_timestamp=0,
            completion_timestamp=5,
        )
        ContentInteractionLog.objects.create(
            user=1,
            start_timestamp=7,
            completion_timestamp=11,
        )
        ContentInteractionLog.objects.create(
            user=1,
            start_timestamp=26,
            completion_timestamp=27,
        )
        self.expected_sum = 10

    def test_class_based_view_cache_sanity(self):
        resp = self.client.get(reverse('summary', kwargs={'user': 1}))
        self.assertEqual(resp.content, '10')
