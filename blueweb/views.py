""" 
Views for blue web.
"""
from django.shortcuts import render
from django.http import HttpResponse
from blueweb import quotes
from blueweb.models import BlogPost, Release, Show, Song
from blueweb.cal import get_cal_for_show

def home(request):
    """ 
    Home page.
    """
    headline = BlogPost.objects.first() if BlogPost.objects.all().exists() else None
    return render(request, 'home.html',context={'headline':headline})

def shows(request):
    """ 
    Show calendar.
    """
    shows = Show.objects.upcoming_shows()
    return render(request, 'shows.html', context={'location':'shows', 'shows':shows})

def music(request):
    """ 
    Music for sale or download.
    """
    releases = Release.objects.all()
    return render(request, 'music.html', context={'location':'music', 'releases':releases})

def news(request):
    """ 
    News of the band.
    """
    posts = BlogPost.objects.all()
    return render(request, 'news.html', context={'location':'news', 'posts':posts})

def about(request):
    """ 
    About page.
    """
    return render(request, 'about.html', context={'location':'about'})

def post(request, post_id, post_slug):
    """ 
    An individual post.
    """
    post = BlogPost.objects.get(pk=post_id)
    return render(request, 'post.html', context={'post':post})

def show_calendar(request, show_id):
    """ 
    Gets an iCalendar event for the specified show.
    """
    show = Show.objects.get(pk=show_id)
    cal = get_cal_for_show(show)
    return HttpResponse(str(cal), content_type='text/calendar')
