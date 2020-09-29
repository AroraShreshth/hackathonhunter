
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from .router import router
from django.conf.urls.static import static
from markdownx import urls as markdownx
from django.contrib.auth import views as auth_views
from .settings import website_name
# Admin.py Stuff
admin.site.site_header = f'{website_name} Admin'
admin.site.site_title = f'{website_name} Admin'
admin.site.index_title = f'{website_name} System Administration'
admin.autodiscover()
admin.site.enable_nav_sidebar = False
urlpatterns = [
    path('', include('users.urls')),
    path('', include('appl.urls')),
    path('issue/', include('issuerep.urls')),
    path('admin/', admin.site.urls),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('competition/', include('comp.urls')),
    path('admin/password_reset/', auth_views.PasswordResetView.as_view(),
         name='admin_password_reset',
         ),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('markdownx/', include('markdownx.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    # Django Debug Toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    # Media Data
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
