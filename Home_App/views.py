from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from Home_App.forms import ContactForm, NewsletterForm
from django.contrib import messages


def index(req):
    return render(req, 'website/index.html')


def about(req):
    return render(req, 'website/about.html')


def contact(req):
    if req.method == 'POST':
        form = ContactForm(req.POST)
        if form.is_valid():
            form.save()
            messages.add_message(req, messages.SUCCESS,'your ticket submitted successfully')
        else:
            messages.add_message(req, messages.ERROR,'your ticket did not submitted')
    form = ContactForm()
    return render(req, 'website/contact.html', {'form': form})


def newsletter_view(req):
    if req.method == 'POST':
        form = NewsletterForm(req.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
