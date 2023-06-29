from django.utils.decorators import method_decorator

from .serializers import PostSerializer, TagSerializer
from .models import Post, Tag
from .permission import IsOwnerOrReadOnly
from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
import logging

logger = logging.getLogger(__name__)


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    search_fields = ('title', 'content', 'author__email', 'tags__name')
    filterset_fields = ('tags', 'author', 'created_at', 'scheduled_time',)
    ordering_fields = ('created_at', 'author')
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @method_decorator(cache_page(60 * 2))
    @method_decorator(vary_on_cookie)
    def dispatch(self, request, *args, **kwargs):
        logger.info("{} sent {} request".format(request.user, request.method))
        return super().dispatch(request, *args, **kwargs)
