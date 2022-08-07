from django.urls import path
from basic import views


urlpatterns= [
    path('reg',views.reg),
    path('log',views.log),
    path('sur',views.sur),

]