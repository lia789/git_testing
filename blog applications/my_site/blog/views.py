from django.shortcuts import render


def home_page(request):
    return render(request, "blog/home_page.html")


def posts(request):
    return render(request, "blog/post_list_page.html")


def post_detail(request, slug):
    return render(request, "blog/post_detail_page.html")
