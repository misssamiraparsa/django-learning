from django.urls import path
from . import views

urlpatterns =[
    path('<int:day>', views.daynamic_day_by_num),
    path('<str:day>', views.daynamic_days),
]