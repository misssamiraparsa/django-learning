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
    'friday': 'this is friday',
}

def days_list(request):
    days_list = list(days.keys())
    list_item = " "
    for day in days_list :
        url_path = reverse('days-of-week', args=[day])
        list_item += f'<li> <a href = "{url_path}">{day} </a> </li>\n'
    contant = f'<ul>\n {list_item}\n</ul>'

    return HttpResponse(contant)

def daynamic_day_by_num(request , day):
    days_name = list(days.keys())
    if day <= len(days_name):
        redirect_day = days_name[day-1]
        redirect_url = reverse('days-of-week', args=[redirect_day])
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseNotFound("day not exists")


def daynamic_days(request , day):
    day_data = days.get(day)
    if day_data is not None:
        #response_data = f'<h1 , style = "color :red" >day is : {day} and data is : {day_data}</h1>'
        response_data = render_to_string('challenges/challenge.html')
        return HttpResponse(response_data)
    return HttpResponseNotFound('day does not exists')



