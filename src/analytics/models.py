from django.db import models

# Create your models here.
from shortener.models import UrlShort


class ClickEventManager(models.Manager):
    def create_event(self, instance):
        if isinstance(UrlShort, instance):
            obj, created = self.get_or_create(shorturl=instance)
            obj.count += 1
            obj.save()
            return obj.count
        return None


class ClickEvent(models.Model):
    shorturl = models.OneToOneField(UrlShort)
    count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ClickEventManager()

    def __str__(self):
        return str(self.count)

    def __unicode__(self):
        return str(self.count)
