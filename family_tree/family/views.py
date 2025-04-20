from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Person

# Create your views here.
def index(request):
    family = Person.objects.order_by("id")
    template = loader.get_template("family/index.html")
    context = {
        "family": family,
    }

    return HttpResponse(template.render(context, request))
