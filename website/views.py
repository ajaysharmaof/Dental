from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.template import loader


def home(request):
	return render(request, 'home.html', {})

def contact(request):

    if request.method == 'POST':
        phone_no = request.POST['phone_no']
        full_name = request.POST['full_name']
        message = request.POST['message']

        message_body = "Full Name - " + full_name + "\n" + "Phone No - " + str(phone_no) + "\n" + message
        img = (('images/t5_image4.jpg','img1'),('images/t5_image5.jpg','img2'),('images/t5_image6.jpg','img3'),('images/t5_image7.jpg','img4'),('images/t5_image8.jpg','img5'),('images/t5_image9.jpg','img6'),('images/t5_bg1.jpg','img7'),('images/t5_bg2.jpg','img8'),('images/t5_ico_email.jpg','img9'),('images/t5_ico_facebook.jpg','img10'),('images/t5_ico_instagram.jpg','img11'),('images/t5_ico_linkedin.jpg','img12'),('images/t5_ico_phone.jpg','img13'),('images/t5_ico_pin.jpg','img14'),('images/t5_ico_twitter.jpg','img15'),)
        html_message = loader.render_to_string("message.html",
        {
            'full_Name' : full_name,
            'phone_no' :  phone_no,
            'Message' : message
        })

        send_mail(full_name, 
        message_body, 
        settings.EMAIL_HOST_USER, 
        ['ajaysharmaof@gmail.com'], 
        fail_silently=False, html_message=html_message
        )
    return render(request, 'contact.html', {})

def about(request):
	return render(request, 'about.html', {})

def blog(request):
	return render(request, 'blog.html', {})

def message(request):
	return render(request, 'message.html', {})

def pricing(request):
	return render(request, 'pricing.html', {})


def service(request):
    	return render(request, 'service.html', {})

def blogdetails(request):
    	return render(request, 'blogdetails.html', {})

