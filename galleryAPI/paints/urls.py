from django.urls import path
from . import views

urlpatterns = [
    path("paints/", views.PaintView.as_view(), name="paints_list"),
]
