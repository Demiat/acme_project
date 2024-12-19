from django.urls import path

from . import views

app_name = 'comments'

urlpatterns = [
    # path('', views.add_comment, name='add_comment'),
    path('', views.CongratulationCreateView.as_view(), name='add_comment'),
]
