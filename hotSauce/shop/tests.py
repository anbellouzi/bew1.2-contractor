import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Sauce


class SauceModelTests(TestCase):

    def test_was_published_recently_with_future_sauce(self):
        """
        was_published_recently() returns False for sauce whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_sauce = Sauce(pub_date=time)
        self.assertIs(future_sauce.was_published_recently(), False)

    def test_was_published_recently_with_old_sauce(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_sauce = Sauce(pub_date=time)
        self.assertIs(old_sauce.was_published_recently(), False)

    def test_was_published_recently_with_recent_sauce(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_sauce = Sauce(pub_date=time)
        self.assertIs(recent_sauce.was_published_recently(), True)
