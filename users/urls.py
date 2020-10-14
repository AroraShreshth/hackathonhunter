from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as user_views
from users.api.auth_views import registerapi, whoami, Logout, profile
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    # Django API AUTH VIEWS
    path('api/auth/register', registerapi, name='api-user-register'),
    path('api/auth/login', obtain_auth_token, name='api-user-login'),
    path('api/auth/whoami', whoami, name='api-user-whoami'),
    path('api/auth/logout', Logout.as_view(), name='api-user-logout'),
    path('api/profile', profile, name='api-profile'),
    # Django AutoComplete Light Views
    path('institute-autocomplete/', user_views.InstituteAutocomplete.as_view(create_field='name'),
         name='institute-autocomplete'),
    path('skill-autocomplete/', user_views.SkillAutocomplete.as_view(create_field='name'),
         name='skill-autocomplete'),
    path('fieldofstudy-autocomplete/', user_views.FieldofStudyAutocomplete.as_view(),
         name='fieldofstudy-autocomplete'),
    path('school-autocomplete/', user_views.SchoolAutocomplete.as_view(create_field='name'),
         name='school-autocomplete'),
    path('city-autocomplete/', user_views.CityAutocomplete.as_view(),
         name='city-autocomplete'),
    # Profile Filling Views
    path('profile/about', user_views.ProfileAbout, name='profile-about'),
    path('profile/preview', user_views.ProfileMarkdown, name='profile-markdown'),
    path('profile/education', user_views.ProfileEducation, name='profile-edu'),
    path('profile/experience', user_views.ProfileExperience, name='profile-exp'),
    path('profile/links', user_views.ProfileLinks, name='profile-links'),
    path('profile/contact', user_views.ProfileContact, name='profile-contact'),
    path('profile/work/create', user_views.ProfileWorkCreate,
         name='profile-work-create'),
    path('profile/skill/connect', user_views.ProfileSkillConnect,
         name='profile-skill-connect'),
    path('profile/resume/upload', user_views.ProfileResumeUpload,
         name='profile-resume-upload'),

    path('profile/work/<uuid:pk>/update', user_views.WorkUpdateView.as_view(),
         name='profile-work-update'),
    path('profile/work/<uuid:pk>/delete',
         user_views.WorkDeleteView.as_view(), name='profile-work-delete'),
    path('profile/skill/<uuid:skill_id>/disconnect',
         user_views.ProfileSkillDisconnet, name='profile-skill-disconnect'),
    path('profile/link/<uuid:pk>/update',
         user_views.LinkUpdateView, name='profile-link-update'),
    path('profile/link/<uuid:link_id>/delete',
         user_views.ProfileLinkDelete, name='profile-link-delete'),
    path('p/', user_views.profilepage, name='public-profile'),
    # Sign Up & On boarding / Welcome Logic & Auth Views
    path('', user_views.homepage, name='home'),
    path('register/', user_views.register, name='register'),
    path('login/', user_views.NewLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='unlogged/logout.html'), name='logout'),
    path('dashboard/', user_views.DashBoard.as_view(), name='dashboard-home'),
    path('about/', user_views.About.as_view(), name='about'),
    path('competitons/', user_views.Explore.as_view(), name='explore'),
    path('help/', user_views.Help.as_view(), name='help'),

    # Settings Panel
    path('settings/about', user_views.settings, name='settings-about'),
    path('settings/photo', user_views.settings_photo, name='settings'),

    path('welcome/name', user_views.welcome, name='dashboard-welcome'),
    path('welcome/verifyemail', user_views.VerifyEmail,
         name='welcome-email-verify'),
    path('welcome/done', user_views.WelcomeDone.as_view(),
         name='welcome-done'),
    path('welcome/about', user_views.welcome_about,
         name='welcome-about'),
    path('terms-of-service/', user_views.TermsofService.as_view(),
         name='terms-of-service'),
    path('privacy-policy/', user_views.PrivacyPolicy.as_view(),
         name='privacy-policy'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='unlogged/password_reset.html'),
         name='password_reset'),
    path('password-reset/done',
         auth_views.PasswordResetDoneView.as_view(
             template_name='unlogged/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confrim/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='unlogged/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='unlogged/password_reset_complete.html'),
         name='password_reset_complete'),
    path('<int:pk>/',
         user_views.UserDetailView.as_view(), name='user-detail'),

]
