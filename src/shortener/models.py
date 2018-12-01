from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

from .utils import code_generator, create_shortcode
from .validators import validate_url, validate_dot_com

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)


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
    url = models.CharField(max_length=220, validators=[validate_url, validate_dot_com])
    shortcode = models.CharField(max_length=SHORTCODE_MAX, default='abc', unique=True, blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UrlShortManager()

    def save(self, *args, **kwargs):
        if self.shortcode == None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(UrlShort, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)

    def get_short_url(self):
        url_path = reverse("scode", kwargs={"shortcode": self.shortcode})
        return "http://localhost:8000" + url_path
