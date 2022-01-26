from ..Controller import *          # Base Controller
from django.apps import apps
from django.http import HttpResponse
from json import loads, dumps, JSONEncoder, JSONDecoder

from logging import config
from app.models.Listing import Listing
from app.models.Realtor import Realtor

class HomeController(Controller):

    def __init__(self):
        pass


    def index(self, request):
        listings = Listing.objects.all()
        context = {
            'listings': listings,
        }
        return render(request, "web/views/index.html", context)


    def about(self, request):
        return render(request, "web/views/about.html")


    def contact(self, request):
        return render(request, "web/views/contact.html")


    def search(self, request):
        return render(request, "web/views/index.html")


    def dashboard(self, request):
        return render(request, 'web/views/dashboard.html')


    def listings(self, request):
        return render(request, 'web/views/listings.html')
    

    def listing(self, request, eid):
        return render(request, 'web/views/listing.html')

