from django.http import HttpResponse
from django.shortcuts import render, redirect
from myapp.models import Article, Motorcycle


def index(request):
    return render(request, "index.html")


def tablas_por_grupos(request):
    return render(request, "tablas_por_grupos.html")


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
    article = Article(title=title, content=content, published=published)

    article.save()

    return HttpResponse(
        f"Articulo creado: {article.title} - {article.content} - {article.published}"
    )


def get_article(request):
    try:
        article = Article.objects.get(
            title="title", content="article content", published=False
        )
        response = f"Article title: {article.title} <br> Content: {article.content}"
    except:
        response = "<h1> article not found </h1>"
    return HttpResponse(response)


def edit_article(request, id):
    article = Article.objects.get(pk=id)

    article.title = "kasawaki"
    article.content = "mustang"
    article.published = True

    article.save()

    return HttpResponse(
        f"Articulo {article.id} editado: {article.title} - {article.content} - {article.published}"
    )


def list_article(request):
    articles = Article.objects.all()

    return render(request, "articles.html", {"articles": articles})


def create_motorcycle(request, brand, reference):
    motorcycle = Motorcycle(brand=brand, reference=reference)

    motorcycle.save()

    return HttpResponse(
        f"The motorcycle {motorcycle.brand} {motorcycle.reference} was created"
    )


def list_motorcycle(request):
    motorcycles = Motorcycle.objects.all()

    return render(request, "motorcycle.html", {"motorcycles": motorcycles})


def del_article(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    return redirect("list-article")
