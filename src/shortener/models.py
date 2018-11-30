from django.db import models
from .utils import code_generator, create_shortcode

# Create your models here.
class UrlShort(models.Model):
    url = models.CharField(max_length=220)
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.shortcode == None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(UrlShort, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)
