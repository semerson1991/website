# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from website import settings
from django.shortcuts import render
from first_choice.models import Video, Image
from django.views.generic.list import ListView

from first_choice.forms import ContactForm
from django.views.decorators.csrf import csrf_exempt

from django.core.mail import EmailMessage
from django.core.mail import send_mail

from django.shortcuts import redirect
from django.template.loader import get_template
from django.contrib import messages


def index(request):
    return render(request, 'personal/home.html')

@csrf_exempt
def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        contact_name = request.POST.get('name')
        contact_email = request.POST.get('email')
        subject = request.POST.get('subject')
        message  = request.POST.get('message')

        template = get_template('personal/contact_template.txt')
        context = {
        'contact_name': contact_name,
        'contact_email': contact_email,
        'subject': subject,
        'form_content': message,
    }
        content = template.render(context)

        email = EmailMessage(
            "New Message from website visitor",
            content,
            "First__Choice",
            [contact_email],
            headers = {'Reply-To': settings.EMAIL_HOST_USER }
        )

        ret = email.send(fail_silently=False)
        messages.success(request, "Email successfully submitted. We will get back to you shortly. ")
        return render(request, 'personal/contact.html', {'form': 'form_class'})
        #return contact_email_sent()

    return render(request, 'personal/contact.html', {'form':'form_class'})


def contact_email_sent(request):
    return render(request, 'personal/contact.html', {'form': 'form_class'})

def about_us(request):
    return render(request, 'personal/about_us.html')

def portfolio(request):
    return render(request, 'personal/portfolio.html')


class ImagesListView(ListView):
    model = Image

class PortfolioView(ListView):
    context_object_name = 'portfolio_list'
    template_name = 'personal/portfolio.html'
    queryset = Image.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PortfolioView, self).get_context_data(**kwargs)
        context['videos'] = Video.objects.all()
        return context