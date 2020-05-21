""" 
Utils for Blue Web.
"""
from django.conf import settings
from datetime import datetime
import pytz


def get_local_now():
    """
    Gets the local TZ (hard-coded to eastern for now), version of now.
    """
    return datetime.now(pytz.timezone(settings.TIME_ZONE))


def localize_dt(raw_datetime):
    """
    Localizes the datetime (hard-coded to eastern for now).
    """
    return get_tz().localize(raw_datetime)


def get_tz():
    """
    Gets the timezone.
    """
    return pytz.timezone(settings.TIME_ZONE)
