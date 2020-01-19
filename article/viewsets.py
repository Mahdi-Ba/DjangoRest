from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter

from . import models
from . import serializers


# Create your views here.
class ArticleViewset(viewsets.ModelViewSet):
    # class ArticleViewset(mixins.ListModelMixin,
    #                      mixins.RetrieveModelMixin,
    #                      mixins.UpdateModelMixin,
    #                      mixins.DestroyModelMixin,
    #                      viewsets.GenericViewSet):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['title']

    @action(detail=False, methods=['GET'], name='Get Highlight')
    def highlight(self, request, *args, **kwargs):
        if self.request.method == 'GET':
            test = request.query_params.get('name')
            return Response(test)
        else:
            return Response("by")


class WriterViewset(viewsets.ModelViewSet):
    queryset = models.Writer.objects.all()
    serializer_class = serializers.WriterSerializer
