from django.shortcuts import render, HttpResponse

navbar = """
        <h1> navbar </h1>
        <ul>
            <li> <a href = "/index"> Index </a> </li>
            <li> <a href = "/show-page"> Show Page </a> </li>
            <li> <a href = "/hello-world"> Hello World </a> </li>  
        </ul>
        <hr>
"""


def index(request):
    return HttpResponse(navbar + """
        <h1> Index </h1>
""")


def hello_world(request):
    return HttpResponse(navbar + "hello world")


def show_page(request):
    return HttpResponse(navbar + """
        <h1> showing page </h1>
        made by <b>mayorcadev</b>
    """)
