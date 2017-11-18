from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("hello there")

def staff(request):
    return render(request, 'forwarder/staff.html')

def apply(request):
    return render(request, 'forwarder/application_form.html')
