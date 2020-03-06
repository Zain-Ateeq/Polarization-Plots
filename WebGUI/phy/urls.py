from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('slider', views.about),
    path('old', views.old),
    path('2_21', views.page2_21),
    path('3_3', views.page3_3),
    path('3_4', views.page3_4),
    path('3_7', views.page3_7)
    ]
