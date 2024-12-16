# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import MyUser

# Добавляем поле с биографией
# к стандартному набору полей (fieldsets) пользователя в админке.
UserAdmin.fieldsets += (
    # Добавляем кортеж, где первый элемент — это название раздела в админке,
    # а второй элемент — словарь, где под ключом fields можно указать нужные поля.
    ('Дополнительные поля', {
        'classes': ('collapse',),
        'fields': ('bio',)
    }
    ),
)
# Регистрируем модель в админке:
admin.site.register(MyUser, UserAdmin)
