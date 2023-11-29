from django.urls import path
from authentication.views import register_view,login_view,logout_view,user_verify_view,otp_view,change_password_view

urlpatterns=[
    path(route='register/',view=register_view,name='register'),
    path(route='login/',view=login_view,name='login'),
    path(route='logout/',view=logout_view,name='logout'),
    path(route='user_verify/',view=user_verify_view,name='user_verify'),
    path(route='otp/<str:token>',view=otp_view,name='otp'),
    path(route='change_password/<str:token>',view=change_password_view,name='change_password'),

]