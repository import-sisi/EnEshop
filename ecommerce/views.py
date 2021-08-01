
from django.http.response import HttpResponse
from django.shortcuts import render 
from django.http import JsonResponse

from ecommerce.forms import ContactForm

def home_page(request):
    # print(request.session.get("first_name", "Unkown"))
    context = {
        "title": "Hello World!"
    }
    return render(request, 'home_page.html', context)

def about_page(request):
    context = {
        "title": "About page"
    }
    return render(request, 'home_page.html', context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "form": contact_form,
        "title": "Cntact page",
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        if request.is_ajax():
            return JsonResponse({"message": "Thank you for your submission"})

    if contact_form.errors:
        errors = contact_form.errors.as_json()
        if request.is_ajax():
            return HttpResponse(errors, status=400, content_type='application/json')

    return render(request, 'contact/view.html', context)

