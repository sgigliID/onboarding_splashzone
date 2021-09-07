from django.contrib.sites.models import Site

from rest_framework import serializers

from news.models import NewsPost
from taxonomy.models import Topic


class DiveSiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Site
        fields = [
            'pk',
            'name',
            'domain',
            'full_url',
        ]


class TopicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topic
        fields = [
            'pk',
            'display_name',
            'internal_name'
        ]


class NewsPostSerializer(serializers.HyperlinkedModelSerializer):
    divesite = DiveSiteSerializer(many=False)
    topics = TopicSerializer(many=True)

    class Meta:
        model = NewsPost
        fields = [
            'pk',
            'title',
            'teaser',
            'publish_date',
            'source',
            'divesite',
            'topics',
        ]
