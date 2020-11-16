""" 
Models for Blue Shift website.
"""
from django.db import models
import datetime
from django.utils.text import slugify
from blueweb.utils import get_local_now, localize_dt


class Release(models.Model):
    """ 
    A music release, probably an album.
    """
    title = models.CharField(max_length=100, unique=True)
    release_date = models.DateField()
    cover_art = models.URLField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    hyperfollow = models.URLField(blank=True, null=True)
    
    def future_release(self):
        """ 
        Checks if this release is in the future.
        """
        release_datetime = localize_dt(datetime.datetime(self.release_date.year, self.release_date.month, self.release_date.day))
        return release_datetime > get_local_now()
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-release_date',)

song_hosting_choices = (
    ('soundcloud', 'SoundCloud'),
    ('bandcamp', 'BandCamp'),
    ('youtube', 'YouTube')
)

class Song(models.Model):
    """ 
    A song.
    """
    release = models.ForeignKey(Release, related_name='songs', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    lyrics = models.TextField(blank=True, null=True)
    snippet = models.CharField(blank=True, null=True, max_length=500)
    ordering = models.IntegerField(default=0)
    link = models.URLField(null=True, blank=True)
    hosting = models.CharField(blank=True, choices=song_hosting_choices, max_length=100)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['ordering']

class BlogPost(models.Model):
    """ 
    A blog post for the website.
    """
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(null=True, blank=True, unique=True)
    link = models.URLField(null=True, blank=True)
    body = models.TextField(blank=True)
    posted = models.DateTimeField(blank=True, default=datetime.datetime.now)
    direct_link = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if self.slug is None and self.title is not None:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-posted',)

class Venue(models.Model):
    """ 
    A place where shows occur.
    """
    name = models.CharField(unique=True, max_length=100)
    address = models.CharField(blank=True, max_length=500)
    link = models.URLField(blank=True)
    
    def __str__(self):
        return self.name


class ShowManager(models.Manager):
    """ 
    Manager for shows.
    """
    def upcoming_shows(self):
        """ 
        Gets shows that haven't already happened.
        """
        now = datetime.datetime.now()
        return self.filter(when__gt=now)

class Show(models.Model):
    """ 
    A live show.
    """
    venue = models.ForeignKey(Venue, related_name='shows', on_delete=models.CASCADE)
    when = models.DateTimeField()
    notes = models.TextField(blank=True)
    
    objects = ShowManager()
    
    def __str__(self):
        return '%s %s  at %s' % (self.when.strftime('%I%p'), self.when.strftime('%A, %B %d %Y'), str(self.venue))
    
    class Meta:
        ordering = ('when',)

class HyperfollowHotlink(models.Model):
    """ 
    A redirect to a hyperfollow page.
    """
    release = models.OneToOneField(Release, related_name="hotlink", on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return f"{self.slug} ({self.release})"
