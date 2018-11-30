import random

from django.db import models


def code_generator(size=6, chars='abcdefghijklmnopqrstuvwxyz'):
    new_code = ''
    for _ in range(size):
        new_code += random.choice(chars)
    return new_code


# Create your models here.
class UrlShort(models.Model):
    url = models.CharField(max_length=220)
    shortcode = models.CharField(max_length=15, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        print('override save')
        super(UrlShort, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)
