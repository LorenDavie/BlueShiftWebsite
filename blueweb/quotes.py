""" 
Quote server.
"""
from random import randint

quote_list = [
    "I was landing on the blue, perpetually in flight.",
    "Everything is fine.",
    "Silence in the skies, no tracks upon the snow.",
    "Eyes red and burning, you can see her stomach turning",
    "I had to fly, to find the source of the wind",
    "Everything I do is wrong, and everyone is judging me",
    "The moments were just wide enough to leave me reeling in doubt",
    "I'm going to buy my way out of these blues",
    "The lie of permanence helps us sleep at night",
]

def random_quote():
    """ 
    Gets a random quote from the list.
    """
    return quote_list[randint(0,len(quote_list)-1)]
