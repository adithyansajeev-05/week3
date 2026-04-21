#from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    return HttpResponse("Wellcome to claw courses!")
def detail_view(request,course_name):
    return HttpResponse(f"you are viewing the couse :{course_name}")
