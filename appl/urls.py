
from django.urls import path
from . import views as appl_views

urlpatterns = [
    path('competitons/explore',
         appl_views.CompListView.as_view(), name='comp-explore')
]
