from django.db import models
from polymorphic.models import PolymorphicModel


class ContentItem(PolymorphicModel):
    """
    Base model for all sorts of content
    """

    title = models.CharField(max_length=250)
    counter = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)

    def increase_counter(self):
        self.counter += 1
        self.save()


class Video(ContentItem):
    """
    Video content model
    """
    video_file = models.CharField(max_length=250)
    srt_file = models.CharField(max_length=250)


class Audio(ContentItem):
    """
    Audio content model
    """
    bitrate = models.IntegerField(null=True)  # suppose bitrate is an integer value?


class Text(ContentItem):
    """
    Text content model
    """
    content = models.TextField(null=True)


class Page(models.Model):
    """
    All page content
    """
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)

    items = models.ManyToManyField(
        ContentItem,
        through='ContentItemOnPage',
        through_fields=('page', 'item'),
        related_name='related_items',
    )


class ContentItemOnPage(models.Model):
    """
    Single content item record (link table)
    """
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    item = models.ForeignKey(ContentItem, on_delete=models.CASCADE)

    # way to setup item's order
    sort_by = models.IntegerField(default=0)

    class Meta:
        ordering = ('sort_by',)
