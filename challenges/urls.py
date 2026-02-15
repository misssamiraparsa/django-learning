from django.urls import path
from . import views

urlpatterns =[
    path('', views.days_list),
    path('<int:day>', views.daynamic_day_by_num),
    path('<str:day>', views.daynamic_days , name='days-of-week'),
]