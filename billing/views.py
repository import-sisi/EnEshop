from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, render
from django.utils.http import is_safe_url
from django.views.decorators.csrf import csrf_exempt


from billing.models import BillingProfile, Card

import stripe
STRIPE_SECRET_KEY = getattr(settings, "STRIPE_SECRET_KEY", "sk_test_51JJfNZB87P9lK1Pvk2Cub1nbWDn2oR4DHelr4at4O1uQlnfB5gTVKzBT2B1uwJzOMlsblyjkJOR6BEcEwfYdHYsO00yG8SvVo1")
STRIPE_PUB_KEY = getattr(settings, "STRIPE_PUB_KEY", 'pk_test_51JJfNZB87P9lK1PvKWwGGjyjMrqirxUTEqwen8RpRFa8VgZWVrqJxp7GqkKMx1cYyIyktTe7m0Msa0rb8sZIrsv300EUXNDHZK')
stripe.api_key = STRIPE_SECRET_KEY

# Create your views here.

def payment_method_view(request):
    #next_url = 
    # if request.user.is_authenticated():
    #     billing_profile = request.user.billingprofile
    #     my_customer_id = billing_profile.customer_id

    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    if not billing_profile:
        return redirect("/cart")
    next_url = None
    next_ = request.GET.get('next')
    if is_safe_url(next_, request.get_host()):
        next_url = next_
    return render(request, 'billing/payment-method.html', {"publish_key": STRIPE_PUB_KEY, "next_url": next_url})

@csrf_exempt
def payment_method_createview(request):
    if request.method == "POST" and request.is_ajax():
        billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
        if not billing_profile:
            return HttpResponse({"message": "Cannot find this user"}, status_code=401)
        token = request.POST.get("token")
        if token is not None:
            new_card_obj = Card.objects.add_new(billing_profile, token)
        return JsonResponse({"message": "Success! Your card was added."})
    return HttpResponse("error", status_code=401)