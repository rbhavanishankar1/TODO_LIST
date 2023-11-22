from django.urls import path
from todo_list.views import *


urlpatterns=[

    path(route='home/',view=home_view,name='home'),
    path(route='update/<id>/',view=update_view,name='upadte'),
    path(route='delete/<id>/',view=delete_view,name='delete'),

]