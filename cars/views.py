from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def cars(request):
    cars = Car.objects.order_by('-created_date')

    paginator = Paginator(cars,4)
    page = request.GET.get('page')
    paged_car = paginator.get_page(page)
    data = {
        # we use this below (commenetd) line when we are feching the data for cars but when we fetching the pagination
        # so use override the cars to paged_car in context
        # 'cars' : paged_car,
        'cars' : paged_car,
    }

    return render(request,'cars/cars.html',data)

def car_details(request,id):
    single_car = get_object_or_404(Car,pk=id)
    data = {
        'single_car': single_car,
    }

    return render(request, 'cars/car_details.html',data)
