from django.urls import path
from friends import views

urlpatterns = [
    path('friends/', views.FriendList.as_view()),
    path('friends/<int:pk>/', views.FriendDetail.as_view())
]