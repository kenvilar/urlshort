from django.db import models
from .utils import code_generator, create_shortcode


# Create your models here.
class UrlShortManager(models.Manager):
    def all(self, *args, **kwargs):
        qs = super(UrlShortManager, self).all(*args, **kwargs)
        qs = qs.filter(active=True)
        return qs

    def refresh_shortcodes(self):
        qs = UrlShort.objects.filter(id__gte=1)
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.shortcode)
            q.save()
            new_codes += 1
        return "New codes made: {i}".format(i=new_codes)


class UrlShort(models.Model):
    url = models.CharField(max_length=220)
    shortcode = models.CharField(max_length=15, default='abc', unique=True, blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UrlShortManager()
    some_random = UrlShortManager()

    def save(self, *args, **kwargs):
        if self.shortcode == None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(UrlShort, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)
