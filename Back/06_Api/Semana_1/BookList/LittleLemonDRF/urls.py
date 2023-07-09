from django.urls import path, include
from . import views


urlpatterns = [
    # path('ratings', views.RatingsView.as_view()),
    path('ratings', views.RatingsView),
]