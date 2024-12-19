from django.contrib import admin
from django.urls import include, path
from django.conf import settings
# Импортируем функцию, позволяющую серверу разработки отдавать файлы.
from django.conf.urls.static import static


handler404 = 'core.views.page_not_found'

urlpatterns = [
    path('', include('pages.urls')),
    path('auth/', include('users.urls')),
    path('<int:pk>/comment/', include('comments.urls')),
    path('admin/', admin.site.urls),
    path('birthday/', include('birthday.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    # Добавить к списку urlpatterns список адресов из приложения debug_toolbar:
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
