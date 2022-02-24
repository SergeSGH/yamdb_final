from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, status, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from users.permissions import IsAdminOrSuper, ReadOnly
from .filters import TitleFilter
from .models import Category, Genre, Title
from .pagination import TitlesPagination
from .serializers import (
    CategorySerializer,
    GenreSerializer,
    TitleInputSerializer,
    TitleOutputSerializer
)


class CategoryViewSet(mixins.CreateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    permission_classes = (IsAdminOrSuper | ReadOnly,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    pagination_class = LimitOffsetPagination
    lookup_field = 'slug'

    def retrieve(self, request, slug=None):
        return Response(status=status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, slug=None):
        return Response(status=status.HTTP_404_NOT_FOUND)


class GenreViewSet(mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    permission_classes = (IsAdminOrSuper | ReadOnly,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    pagination_class = LimitOffsetPagination
    lookup_field = 'slug'


class TitleViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrSuper | ReadOnly,)
    queryset = Title.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter
    pagination_class = TitlesPagination

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'partial_update':
            return TitleInputSerializer
        return TitleOutputSerializer
