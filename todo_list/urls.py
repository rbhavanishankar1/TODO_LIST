from django.urls import path
from todo_list.views import home_view,update_view,delete_view


urlpatterns=[

    path(route='home/',view=home_view,name='home'),
    path(route='update/<id>/',view=update_view,name='upadte'),
    path(route='delete/<id>/',view=delete_view,name='delete'),

]