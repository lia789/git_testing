from django.shortcuts import render



def starting_page(request):
    return render(request, "blog/home_page.html")

def posts(request):
    return render(request, "blog/blog_list_page.html")


def post_detail(request):
    return render(request, "blog/blog_page.html")
