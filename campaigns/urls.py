from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.campaign_list,
        name='campaign_list'
    ),

    path(
        '<int:id>/',
        views.campaign_detail,
        name='campaign_detail'
    ),

]