from django.urls import path
from follows import views

urlpatterns = [
    path('follows/', views.followList.as_view()),
    path('follows/<int:pk>/', views.followDetail.as_view())
]