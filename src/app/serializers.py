from rest_framework import serializers

from app.models import Page, ContentItem, Video, Audio, Text


class PageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Page
        fields = ('title', 'url')


class VideoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('title', 'video_file', 'srt_file', 'counter',)


class AudioItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = ('title', 'bitrate', 'counter',)


class TextItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = ('title', 'content', 'counter',)


class ContentItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentItem
        fields = '__all__'

    def to_internal_value(self, data):
        pass

    def to_representation(self, value):
        if isinstance(value, Video):
            return VideoItemSerializer(instance=value).data
        elif isinstance(value, Audio):
            return AudioItemSerializer(instance=value).data
        elif isinstance(value, Text):
            return TextItemSerializer(instance=value).data


class SinglePageSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()

    def get_items(self, instance):
        """
        We have to respect order in intermediate model
        :param instance:
        :return:
        """
        sorted_items = instance.items.order_by('contentitemonpage__sort_by').all()
        return ContentItemSerializer(sorted_items, read_only=True, many=True).data

    class Meta:
        model = Page
        fields = ('title', 'items')
