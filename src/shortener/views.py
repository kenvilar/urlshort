from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


# Create your views here.
def urlshort_redirect_view(request, shortcode=None, *args, **kwargs): #function based view
    return HttpResponse("Hello {sc}".format(sc=shortcode))


class UrlShortClassBasedView(View): #class based view
    def get(self, request, shortcode=None, *args, **kwargs):
        return HttpResponse("Hello again {sc}".format(sc=shortcode))
