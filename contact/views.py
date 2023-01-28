from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User
# Create your views here.

def inquiry(request):

    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        city = request.POST['city']
        state = request.POST['state']
        phone = request.POST['phone']
        email = request.POST['email']
        customer_need = request.POST['customer_need']
        message = request.POST['message']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_request = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_request:
                messages.error(request, 'You already reuested for same car. Please wait we will contact you.')
                return redirect('/cars/'+car_id)

        # here we are sending the data to model (database)
        # here we use firstname bcz in the model we use it not first_name.
        contact = Contact(car_id=car_id, car_title=car_title, user_id=user_id, firstname=first_name, lastname=last_name,
        city=city, state=state, phone=phone, email=email, customer_need=customer_need, message=message)

        # we are fetching super user email id
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email

        send_mail(
                'New Car Inquiry',
                'You have new inquiry for the car',
                'vishdatodiya12@gmail.com',
                [admin_email],
                # ['vishaldatodiya12@gmail.com'],      # this is working fine
                fail_silently=False,
            )


        contact.save()
        messages.success(request,'Your request has been submitted. We will get back to you shortly.')
        return redirect('/cars/'+car_id)
