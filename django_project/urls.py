from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("pages/", include("pages.urls")),
    path("", include("articles.urls")),
    path("character/", include("dnd_character.urls")),
    path("fediverse/", include("fediverse.urls")),
    path("calculator/", include("calculator.urls")),
    path("tasks/", include("htmx_tasks.urls")),
]

if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
