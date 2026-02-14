from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect

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

def daynamic_day_by_num(request , day):
    days_name = list(days.keys())
    if day <= len(days_name):
        redirect_day = days_name[day-1]
        return HttpResponseRedirect(f'/days/{redirect_day}')
    else:
        return HttpResponseNotFound("day not exists")
    #return HttpResponse(day)


def daynamic_days(request , day):
    day_data = days.get(day)
    if day_data is not None:
        return HttpResponse(
        f'day is : {day} and data is : {day_data}')
    return HttpResponseNotFound('day does not exists')