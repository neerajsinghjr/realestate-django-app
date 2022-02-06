from typing import List
from ..Controller import *          # Base Controller
from django.apps import apps
from django.http import Http404, HttpResponse
from json import loads, dumps, JSONEncoder, JSONDecoder
from logging import config
from django.http import HttpResponseRedirect

from app.models.Listing import Listing
from app.models.Realtor import Realtor


class HomeController(Controller):

    def __init__(self):
        pass


    def index(self, request):
        try:
            listings = Listing.objects.all()
            context = {
                'listings': listings,
            }
            return render(request, "web/views/index.html", context)

        except Listing.DoesNotExist:
            raise Http404("404:Listing not found")


    def about(self, request):
        try :
            realtors = Realtor.objects.all()                            # Realtors
            topSeller = realtors.filter(top_seller = True).get()        # Top Seller
            context = {
                'realtors' : realtors,
                'topSeller' : topSeller,
            }
            return render(request, "web/views/about.html", context)

        except Realtor.DoesNotExist:
            raise Http404("404:Realtor not found")


    def contact(self, request):
        return render(request, "web/views/contact.html")


    def search(self, request):
        return render(request, "web/views/index.html")


    def dashboard(self, request):
        return render(request, 'web/views/dashboard.html')


    def listings(self, request):
        try:
            listings = Listing.objects.all()
            context = {
                'listings': listings,
            }
            return render(request, 'web/views/listings.html', context)

        except Listing.DoesNotExist:
            raise Http404('404:Listings not found')


    def listing(self, request, eid):
        try:
            listing = Listing.objects.get(pk=eid)
            context = {
                'listing' : listing,
            }
            return render(request, 'web/views/listing.html', context)

        except Listing.DoesNotExist:
            raise Http404('404:Listing not found')


    def httpBack(self, request):
        return HttpResponse(str(request.META.get('HTTP_REFERER')))
        # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


    def realtor(self, request, eid):
        try:
            realtor = Realtor.objects.get(pk=eid)
            listings = realtor.listing_set.all()
            context = {
                'realtor' : realtor,
                'listings' : listings,
            }
            return render(request, 'web/views/realtor.html', context)

        except Listing.DoesNotExist:
            raise Http404("404:Listing not found")

