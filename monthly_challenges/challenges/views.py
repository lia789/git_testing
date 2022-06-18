from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


every_month_task = {
    "january": "Playing badminton and reading book (January)",
    "february": "Fall in love some one (February)",
    "march": "Find new job or projects (March)",
    "april": "Earn lot of money (April)",
    "may": "Ready for Eid (May)",
    "may": None,
    "june": "Close all pending task in (June)",
    "july": "Learn new things about machine learnings (July)",
    "august": "Switch company (August)",
    "september": "Your birthday month (September)",
    "october": "Play cricket (October)",
    "november": "Enjoy weather (November)",
    "december": "Sleep and sleep (December)",
}


def index(request):
    months = list(every_month_task.keys())
    return render(request, "challenges/index.html", {"months": months})


def monthly_challenges(request, month):
    try:
        month_goal_text = every_month_task[month]
        return render(request, "challenges/challenges.html", {"month_goal_text": month_goal_text, "month":month})
    except:
        response_not_found_html = """
        <h1>Invalid Month names!</h1>
        <h4>try valid month name ..</h4>
        """
        return HttpResponseNotFound(response_not_found_html)


def monthly_challenges_url_number_version(request, month):
    try:
        months = list(every_month_task.keys())
        redirect_month = months[month-1]
        redirect_path = reverse("month-challenge", args=[redirect_month])

        return HttpResponseRedirect(redirect_path)
    except:
        response_not_found_html = """
            <h1>Invalid Month number!</h1>
            <h4>try valid month number ..</h4>
        """
        return HttpResponseNotFound(response_not_found_html)