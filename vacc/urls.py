
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from .router import router
from django.conf.urls.static import static
from markdownx import urls as markdownx

urlpatterns = [
    path('', include('users.urls')),
    path('admin/', admin.site.urls),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
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
