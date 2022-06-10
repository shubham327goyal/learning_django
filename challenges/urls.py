from django.urls import path
from . import views

urlpatterns = [
    path("<int:monthwise>", views.monthwiseno),
    path("<str:monthwise>", views.monthwise),
]
