from django.urls import include, path, reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LogoutView

from .forms import CustomUserCreationForm


urlpatterns = [
    path(
        'registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=CustomUserCreationForm,
            success_url=reverse_lazy('pages:homepage'),
        ),
        name='registration',
    ),
    path('logout/', LogoutView.as_view(
        template_name='registration/logged_out_auth.html'),
        name='auth_logout'),
    path('', include('django.contrib.auth.urls')),
]
