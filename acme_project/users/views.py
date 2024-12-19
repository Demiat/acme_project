from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm


class RegisterUserView(CreateView):
    template_name = 'registration/registration_form.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)

        # Отправляем письмо после успешной регистрации
        send_mail(
            'Успешная регистрация',
            'Поздравляем! Вы успешно зарегистрировались на нашем сайте.', 
            'noreply@example.com', 
            (form.cleaned_data['email'],), 
            fail_silently=True
        )

        return response