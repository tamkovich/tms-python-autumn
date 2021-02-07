from django.contrib.auth.models import User

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.pagination import LimitOffsetPagination

from home.models import Article

from api.pagination import CustomPageNumberPagination
from api.permissions import IsAuthorOrReadOnly
from api.serializers import ArticleSerializer, UserSerializer


class ArticleViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated, IsAuthorOrReadOnly)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'content')


class UserViewSet(ModelViewSet):
    # permission_classes = (IsAdminUser, )
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "username"
    pagination_class = LimitOffsetPagination
