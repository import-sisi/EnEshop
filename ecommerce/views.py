
from django.shortcuts import render 

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

    if contact_form.is_valid():
        # full_name = contact_form.cleaned_data.get('full_name')
        # email = contact_form.cleaned_data.get('email')
        # subject = contact_form.cleaned_data.get('subject')
        # text = contact_form.cleaned_data.get('text')
        # ContactUs.objects.create(full_name=full_name, email=email, subject=subject, text=text, is_read=False)
        # todo : show user a success message
        contact_form = ContactForm()

    context = {
        "form": contact_form,
        "title": "Cntact page",

    }
    # if request.method == "POST":
    #     # print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request, 'contact/view.html', context)

