from django.urls import path

from user_profile import views

urlpatterns = [
    path('<str:username>/', views.UserDetailView.as_view(), name='user-profile'),
    path('<str:username>/edit/', views.UserUpdateView.as_view(), name='edit-profile'),
    path('<str:username>/delete/', views.UserDeleteView.as_view(), name='delete-profile')
]
