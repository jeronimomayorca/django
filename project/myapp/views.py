from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import Article


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


def create_article(request, title, content, published):
    article = Article(
        title=title,
        content=content,
        published=published
    )

    article.save()

    return HttpResponse(f"Articulo creado: {article.title} - {article.content} - {article.published}")


def get_article(request):
    try:
        article = Article.objects.get(title='title', content='article content', published=False)
        response = f"Article title: {article.title} <br> Content: {article.content}"
    except:
        response = "<h1> article not found </h1>"
    return HttpResponse(response)
