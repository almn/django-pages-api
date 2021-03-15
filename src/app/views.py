from rest_framework import generics

from app.models import Page
from app.serializers import PageSerializer, SinglePageSerializer
from app.tasks import increase_page_counters


class PageList(generics.ListAPIView):
    """
    Page list API endpoint
    """
    model = Page
    serializer_class = PageSerializer
    queryset = Page.objects.all()


class PageDetail(generics.RetrieveAPIView):
    """
    Single Page API endpoint
    """
    model = Page
    serializer_class = SinglePageSerializer
    queryset = Page.objects.order_by('contentitemonpage__sort_by').all()

    def retrieve(self, request, *args, **kwargs):
        # set async task to page_view
        increase_page_counters.delay(kwargs['pk'])

        return super().retrieve(request, *args, **kwargs)


