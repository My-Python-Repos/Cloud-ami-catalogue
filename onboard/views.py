# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import OnboardRequest
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt



# Create your views here.
@csrf_exempt
def onboard(request):
    if request.method == 'POST':
        first = request.POST.get('first_name')
        last = request.POST.get('last_name')
        phone = request.POST.get('phone_number')
        em = request.POST.get('email')
        new_onboard = OnboardRequest(first_name=first, last_name = last, phone_number = phone, email = em)
        new_onboard.save()
    return render(request, 'onboard.html')
