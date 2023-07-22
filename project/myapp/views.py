from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def contact(request):
    return render(request, "contact.html")


def about_me(request):
    qualities = ["clever", "cheerful", "analytical"]

    return render(request, "about_me.html", {"qualities": qualities})


def say_hi(request):
    num = 46
    is_even = False

    if num % 2 == 0:
        is_even = True

    return render(request, "say_hi.html", {"is_even": is_even, "num": num})
