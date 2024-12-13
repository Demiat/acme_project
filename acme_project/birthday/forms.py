from django import forms
from django.core.exceptions import ValidationError

from .models import Birthday


class BirthdayForm(forms.ModelForm):
    # first_name = forms.CharField(label='Имя', max_length=20)
    # last_name = forms.CharField(
    #     label='Фамилия', required=False, help_text='Необязательное поле'
    # )
    # birthday = forms.DateField(
    #     label='Дата рождения',
    #     # Указываем, что виджет для ввода даты должен быть с типом date.
    #     widget=forms.DateInput(attrs={'type': 'date'})
    # )

    class Meta:
        # Указываем модель, на основе которой должна строиться форма.
        model = Birthday

        fields = '__all__'

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_first_name(self):
        # Получаем значение имени из словаря очищенных данных.
        first_name = self.cleaned_data['first_name']
        # Разбиваем полученную строку по пробелам
        # и возвращаем только первое имя.
        return first_name.split()[0]

    def clean(self):
        # Вызов родительского метода clean.
        # В том числе чтобы сработали ограничения модели
        super().clean()
        BEATLES = {'Джон Леннон', 'Пол Маккартни',
                   'Джордж Харрисон', 'Ринго Старр'}
        # Получаем имя и фамилию из очищенных полей формы.
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        # Проверяем вхождение сочетания имени и фамилии во множество имён.
        if f'{first_name} {last_name}' in BEATLES:
            raise ValidationError(
                'Мы тоже любим Битлз, но введите, пожалуйста, настоящее имя!'
            )
