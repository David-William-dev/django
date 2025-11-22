from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse


# Create your views here.
def homePage(request):
    return render(request=request,template_name="html/home.html")


def getFine(req):
    return HttpResponse("I am fine")


def dynamicUrl(req, id):
    return HttpResponse(f"ID is {id}")


def redirectUrl(req):
    return redirect(reverse("are_you_fine"))
