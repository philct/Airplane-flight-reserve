from django.shortcuts import render, redirect
from django import forms
from .models import Airport, Flight, Passenger

# Create your views here.
def index(request):
    return render(request, 'flights/index.html', {
        'flights': Flight.objects.all()
    })

def details(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    return render(request, 'flights/details.html', {
        'flight': flight,
        'passengers': flight.passengers.all(),
        'non_passengers': Passenger.objects.exclude(flight=flight),
    })

def add(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    if request.method == 'POST':
        non_passenger = request.POST['non_passenger']
        flight.passengers.add(non_passenger)
        return redirect('flights:details', flight_id=flight_id)
    
    return render(request, "flights/add.html", { 
        'flight': flight,
        'non_passengers': Passenger.objects.exclude(flight=flight ),
        })