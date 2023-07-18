from django.shortcuts import render, HttpResponse

navbar = """

"""


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def about_me(request):
    return render(request, 'about_me.html')


# view with parameters and optional parameters
def say_hi(request, name='', surname=''):
    return HttpResponse(navbar + f"Hello {name} {surname}")
