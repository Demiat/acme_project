from django.urls import include, path
from django.contrib.auth.views import LogoutView

from .views import RegisterUserView


urlpatterns = [
    path(
        'registration/',
        RegisterUserView.as_view(),
        name='registration',
    ),
    path('logout/', LogoutView.as_view(
        template_name='registration/logged_out_auth.html'),
        name='auth_logout'),
    path('', include('django.contrib.auth.urls')),
]
