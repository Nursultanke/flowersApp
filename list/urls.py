from django.urls import path
from .views import FlowerView
app_name = "flowers"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('flowers/', FlowerView.as_view()),
]