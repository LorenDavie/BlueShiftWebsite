""" 
Calendar functions
"""
from ics import Calendar, Event
from datetime import timedelta


def get_cal_for_show(show):
    """ 
    Gets a calendar for the specified show.
    """
    c = Calendar()
    e = Event()
    e.name = 'Blue Shift at %s' % show.venue.name
    e.begin = show.when
    e.end = show.when + timedelta(hours=1)
    e.location = '%s %s' % (show.venue.name, show.venue.address)
    c.events.add(e)
    return c
