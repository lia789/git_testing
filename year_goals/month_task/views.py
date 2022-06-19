from django.shortcuts import render


monthly_task =  {
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


def home_page(request):
    month_name_lits = list(monthly_task.keys())
    return render(request, "month_task/index.html", {"months":month_name_lits})



def month_task(request, month):
    try:
        task_text = monthly_task[month]
        return render(request, "month_task/task.html", {"task_text": task_text, "month_name": month})
    except:
        return render(request, '404.html')

