from issuerep import views as issue_views
from django.urls import path

urlpatterns = [
    # Issue Views
    path('create/', issue_views.CreateIssue.as_view(), name='issue-create'),
    path('your/', issue_views.YourIssues.as_view(), name='issue-yours'),
    path('', issue_views.IssueList.as_view(), name='issue-list'),
    path('<uuid:pk>/', issue_views.IssueDetail.as_view(),
         name='issue-detail'),
    path('<uuid:pk>/update/',
         issue_views.IssueUpdateView.as_view(), name='issue-update'),
    path('<uuid:pk>/delete/',
         issue_views.IssueDeleteView.as_view(), name='issue-delete'),
]
