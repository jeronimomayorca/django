from django.shortcuts import render, HttpResponse

navbar = """
    <h1> Navbar </h1>
    <ul>
        <li> <a href="/index"> Index </a> </li>
        <li> <a href="/contact"> Contact </a> </li>
        <li> <a href="/about-me"> About Me </a> </li>
    </ul>
"""


def index(request):
    return HttpResponse(navbar + "Index")


def contact(request):
    return HttpResponse(navbar + "Contact")


def about_me(request):
    return HttpResponse(navbar + "About me")
