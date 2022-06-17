from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenge_list = {
    "january": "January text",
    "february": "february text",
    "march": "march text",
    "april": "april text",
    "may": "may text",
    "june": "june text",
    "july": "july text",
    "august": "august text",
    "september": "september text",
    "october": "october text",
    "november": "november text",
    "december": "december text"
}


def index(request):

    html_list_tag = ""

    months = list(monthly_challenge_list.keys())

    for month in months:
        capitalized_month = month.capitalize()
        url_path = reverse("month-challenge", args=[month])
        html_list_tag += f"<li><a href=\"{url_path}\">{capitalized_month}</a></li>"

    html = f"<ul>{html_list_tag}</ul>"

    return HttpResponse(html)


def monthly_challenges_int(request, month):
    months = list(monthly_challenge_list.keys())
    if month > len(months):
        return HttpResponseNotFound("Month number not valid")

    redirect_month = months[month-1]

    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenges(request, month):
    try:
        challenges_text = monthly_challenge_list[month]
        return HttpResponse(challenges_text)
    except:
        return HttpResponseNotFound("This month is not supported")
