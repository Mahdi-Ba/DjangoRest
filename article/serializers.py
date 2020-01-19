from rest_framework import serializers
from .models import Article, Writer


class WriterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Writer
        # fields = '__all__'
        fields = ['name', 'family']


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    # auther = serializers.StringRelatedField()
    auther = WriterSerializer()

    class Meta:
        model = Article
        fields = ['id', 'title', 'auther', 'url']
