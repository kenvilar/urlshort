from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import UrlShort
from .forms import SubmitUrlForm


# Create your views here.
def home_functionbasedview(request, *args, **kwargs):
    if request.method == "POT":
        print(request.POST)
    return render(request, "shortener/home.html", {})


class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitUrlForm()
        context = {
            "title": "URL SHORT",
            "form": the_form
        }
        return render(request, "shortener/home.html", context)

    def post(self, request, *args, **kwargs):
        # print(request.POST)
        # print(request.POST.get("url"))
        # print(request.POST["url"])
        form = SubmitUrlForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data.get("url"))
        context = {
            "title": "URL SHORT",
            "form": form
        }
        return render(request, "shortener/home.html", context)


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


class UrlShortClassBasedView(View):  # class based view
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(UrlShort, shortcode=shortcode)
        return HttpResponse("Hello again {sc}".format(sc=obj.url))


def test_view(request):
    return HttpResponse("Some stuff")
