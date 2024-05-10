from django.http import HttpResponse


# Create your views here.
# a django component that handles a request for a web page

# normal python function with unused request.
# view function, handles http request of the Welcome Page of the site
# when a user visits the welcome page, the HttpResponse will be displayed
def welcome(request):
    return HttpResponse("Welcome to the Meeting Planner!")


def about(request):
    return HttpResponse("I'm a software engineer")
