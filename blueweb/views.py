""" 
Views for blue web.
"""
from django.shortcuts import render
from django.http import HttpResponse
from blueweb import quotes

def home(request):
    """ 
    Home page.
    """
    return render(request, 'home.html', context={})

def quote(request):
    """ 
    Gets a random quote.
    """
    return HttpResponse(quotes.random_quote())

def shows(request):
    """ 
    Show calendar.
    """
    return render(request, 'shows.html', context={'location':'shows'})
