from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views


router = DefaultRouter()
router.register(
    'articles', views.ArticleViewSet, basename="articles"
)
router.register(
    'users', views.UserViewSet, basename="users"
)
"""
/articles/ - GET / List
/articles/ - POST / Create
/articles/<int:pk>/ - GET / Read
/articles/<int:pk>/ - DELETE / Delete
/articles/<int:pk>/ - PUT / Update
"""


urlpatterns = [
    path('', include(router.urls)),
]
