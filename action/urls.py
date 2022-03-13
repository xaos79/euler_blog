from django.urls import path
from . import views

app_name = 'action'
urlpatterns = [
    path('', views.HomeList.as_view(), name='home'),
    path("detail/<int:pk>/", views.SolutionDetailView.as_view(), name='detail'),
]
