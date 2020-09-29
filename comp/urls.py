from django.urls import path
from . import views as comp_views

urlpatterns = [
    path('', comp_views.Start.as_view(), name='comp-start'),
    path('pricing/', comp_views.Pricing.as_view(), name='comp-start'),
]
