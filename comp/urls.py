from django.urls import path
from . import views as comp_views

urlpatterns = [
    path('start/', comp_views.Start.as_view(), name='comp-start')
]
