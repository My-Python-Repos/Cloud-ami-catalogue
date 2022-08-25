from django.http import HttpResponse
from .models import Ami, Update
from django.shortcuts import render
from django.db.models import Q
import ast
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    #ami_listing = Ami.objects.order_by('-creation_date')[:10]
    query = request.GET.get("q")
    platform = request.GET.get("platform")
    if query:
        ami_listing = Ami.objects.filter(
            Q(ami_name__icontains=query) |
            Q(platform__icontains=query) |
            Q(creation_date__icontains=query) |
            Q(ami_id__icontains=query)).distinct().order_by('-creation_date')[:10]
    elif platform:
        ami_listing = Ami.objects.filter(Q(platform__icontains=platform)).distinct().order_by('-creation_date')[:10]
    else:
        ami_listing = Ami.objects.order_by('-creation_date')[:10]
    return render(request, 'ami_info/index.html', {'ami_listing': ami_listing})

def detail(request, ami_id_used):
    ami = Ami.objects.get(ami_id=ami_id_used)
    return render(request, 'ami_info/detail.html', {'ami':ami})

@csrf_exempt
def make_update(request):
    # curl http://127.0.0.1:8000/make_update --data '{"text":"test_update_text", "ami":"ami-4ddcf436"}'
    if request.method == 'POST':
        update_data = ast.literal_eval(request.body)
        new_update = Update(text=update_data['text'], ami=Ami.objects.get(ami_id=update_data['ami']))
        new_update.save()
        return HttpResponse("Creating update page.")


@csrf_exempt
def make_ami(request):
    # curl http://127.0.0.1:8000/make_ami --data '{"ami_name":"test_ami","ami_id":"ami-3dfgcdtx","platform":"mikeplat"}'
    if request.method == 'POST':
        ami_data = ast.literal_eval(request.body)
        #Already exists - this shouldn't happen
        if (len(Ami.objects.filter(ami_id=ami_data['ami_id'])) > 0):
            return HttpResponse("Already an existing AMI - not saving AMI")
        else:
            new_ami = Ami(ami_name=ami_data['ami_name'], ami_id=ami_data['ami_id'], platform = ami_data['platform'])
            new_ami.save()
        return HttpResponse("Creating ami page.")
