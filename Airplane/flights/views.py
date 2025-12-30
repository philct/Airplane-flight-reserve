from django.shortcuts import render, redirect
from django.http import request
from .models import Airport, Flight

# Create your views here.
def index(request):
    return render(request, 'flights/index.html', {
        'flights': Flight.objects.all()
    })

def details(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    return render(request, 'flights/details.html', {
        'flight': flight,
    })