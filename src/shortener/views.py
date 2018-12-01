from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import UrlShort


# Create your views here.
def urlshort_redirect_view(request, shortcode=None, *args, **kwargs):  # function based view
    # (option 1) Plain way
    # obj_url = UrlShort.objects.get(shortcode=shortcode)

    # (option 2) Try--exception
    # try:
    #     obj_url = UrlShort.objects.get(shortcode=shortcode)
    # except:
    #     obj_url = UrlShort.objects.all().first()

    # (option 3) With a default value 'None'
    # obj_url = None
    # qs = UrlShort.objects.filter(shortcode__iexact=shortcode.upper())
    # if qs.exists() and qs.count() == 1:
    #     obj = qs.first()
    #     obj_url = obj.url

    # (option 3) using 'get_object_or_404'
    obj = get_object_or_404(UrlShort, shortcode=shortcode)
    obj_url = obj.url

    return HttpResponseRedirect(obj_url)


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "shortener/home.html", {})


class UrlShortClassBasedView(View):  # class based view
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(UrlShort, shortcode=shortcode)
        return HttpResponse("Hello again {sc}".format(sc=obj.url))


def test_view(request):
    return HttpResponse("Some stuff")
