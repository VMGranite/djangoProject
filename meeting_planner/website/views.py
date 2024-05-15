from django.http import HttpResponse
from django.shortcuts import render

from meetings.models import Meeting


# Create your views here.
# a django component that handles a request for a web page

# normal python function with unused request.
# view function, handles http request of the Welcome Page of the site
# when a user visits the welcome page, the HttpResponse will be displayed
def welcome(request):
    if request.user.is_authenticated:
        context = {"meetings": Meeting.objects.all()}
    else:
        context = {}
    return render(request, "website/welcome.html", context=context)


def about(request):
    return HttpResponse("I'm a software engineer")
