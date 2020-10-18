from django.urls import path
from invite.api import api_views

urlpatterns = [
    path('api/invite/add', api_views.getinvite, name='api-invite-view')
]
