from users.api import viewsets as user_viewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('snippets', user_viewset.SnippetViewSet, basename='snippet')
# router.register(r'users', user_viewset.UserViewSet, basename='user')
router.register(r'city', user_viewset.CityViewSet, basename='city')
router.register(r'institute', user_viewset.InstituteViewSet,
                basename='institute')
router.register(r'fieldofstudy', user_viewset.FieldofStudyViewSet,
                basename='fieldofstudy')
router.register(r'skill', user_viewset.SkillViewSet,
                basename='skill')
router.register(r'school', user_viewset.SchoolViewSet,
                basename='school')
