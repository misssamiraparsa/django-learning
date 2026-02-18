from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

#create Dictionary
days = {
    'saturday': 'this is saturday',
    'sunday': 'this is sunday',
    'monday': 'this is monday',
    'tuesday': 'this is tuesday',
    'wednesday': 'this is wednesday',
    'thursday': 'this is thursday',
    'friday':None,
}

def days_list(request):
    days_list = list(days.keys())
    context = {
        'days': days_list
    }
    return render(request,"challenges/index.html", context)

def daynamic_day_by_num(request, day):
    days_name = list(days.keys())
    if day <= len(days_name):
        redirect_day = days_name[day-1]
        redirect_url = reverse('days-of-week', args=[redirect_day])
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseNotFound("day not exists")


def daynamic_days(request, day):
    day_data = days.get(day)
    context = {
            "data": day_data,
            "day": day
        }
    return render(request,'challenges/challenge.html', context)



