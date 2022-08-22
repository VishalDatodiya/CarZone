from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def cars(request):
    cars = Car.objects.order_by('-created_date')

    paginator = Paginator(cars,4)
    page = request.GET.get('page')
    paged_car = paginator.get_page(page)

    # cars small search pages
    model_search = Car.objects.values_list('model',flat=True).distinct()
    year_search = Car.objects.values_list('year',flat=True).distinct()
    city_search = Car.objects.values_list('city',flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style',flat=True).distinct()

    data = {
        # we use this below (commenetd) line when we are feching the data for cars but when we fetching the pagination
        # so use override the cars to paged_car in context
        # 'cars' : paged_car,
        'cars' : paged_car,
        'model_search': model_search,
        'year_search':year_search,
        'city_search':city_search,
        'body_style_search':body_style_search,
    }

    return render(request,'cars/cars.html',data)

def car_details(request,id):
    single_car = get_object_or_404(Car,pk=id)
    data = {
        'single_car': single_car,
    }

    return render(request, 'cars/car_details.html',data)


def search(request):
    cars = Car.objects.order_by('-created_date')

    model_search = Car.objects.values_list('model',flat=True).distinct()
    year_search = Car.objects.values_list('year',flat=True).distinct()
    city_search = Car.objects.values_list('city',flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style',flat=True).distinct()
    transmission_search = Car.objects.values_list('transmission',flat=True).distinct()


    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)
    # data = {
    #     'cars': cars,
    # }

    # here we are checking the model which is passes from the URL (request)

    # Note : here this model, city .... this name is come from model.py name.
    # in min_price you have to use price bcz you used price as a variable name in models.py

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact=model)
    # data = {
    #     'cars': cars,
    # }

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            cars = cars.filter(city__iexact=city)
    # data = {
    #     'cars': cars,
    # }

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)
    # data = {
    #     'cars': cars,
    # }

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)
    # data = {
    #     'cars': cars,
    # }

    if 'transmission' in request.GET:
        transmission = request.GET['transmission']
        if transmission:
            cars = cars.filter(transmission__iexact=transmission)

    # data = {
    #     'cars': cars,
    # }

    
    # min and max price


    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)



    data = {
        'cars': cars,
        'model_search': model_search,
        'year_search':year_search,
        'city_search':city_search,
        'body_style_search':body_style_search,
        'transmission_search':transmission_search,
    }

    return render(request,'cars/search.html',data)
