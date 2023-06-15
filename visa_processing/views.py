from django.shortcuts import render
from .models import Visa


# Create your views here.
def list(request):
    list = Visa.objects.all()
    return render(request, "visa_processing/visa_processing_list.html", {'visa_processing_list':list})

def add(requests):
    pass


def update(requests):
    pass


def delete(requests):
    pass