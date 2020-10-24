from users.api import viewsets as user_viewset
from issuerep.api import viewsets as issuerep_viewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('snippets', user_viewset.SnippetViewSet, basename='snippet')
# router.register(r'users', user_viewset.UserViewSet, basename='user')
router.register(r'city', user_viewset.CityViewSet, basename='city')
router.register(r'institute', user_viewset.InstituteViewSet,
                basename='institute')
router.register(r'fieldofstudy', user_viewset.FieldofStudyViewSet,
                basename='fieldofstudy')
router.register(r'skill', user_viewset.SkillViewSet, basename='skill')
router.register(r'school', user_viewset.SchoolViewSet, basename='school')
router.register(r'work', user_viewset.WorkViewSet, basename='work')
router.register(r'link', user_viewset.LinkViewSet, basename='link')
router.register(r'issuetype', issuerep_viewset.IssueTypeViewSet,
                basename='issuetype')
router.register(r'issue', issuerep_viewset.IssueViewSet, basename='issue')
router.register(r'contact', user_viewset.ContactViewSet, basename='contact')
router.register(r'banner', user_viewset.BannerViewSet, basename='banner')
