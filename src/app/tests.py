import json

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from app.models import Page, Audio, Video, Text


class PageTest(TestCase):
    """
    ORM tests
    """

    def setUp(self) -> None:
        Page.objects.create(title='Test Page 1')

        items = [(Audio.objects.create(title='audio 1', bitrate=100)),
                 (Video.objects.create(title='video 1', video_file='video1.mkv', srt_file='srt.srt')),
                 (Text.objects.create(title='text 1', content='Long text content'))]

        page = Page.objects.create(title='Test Page 2')
        page.items.set(items)

    def test_page_created(self):
        """
        empty page creation test
        """

        page_found = Page.objects.get(title='Test Page 1')

        self.assertEqual(page_found.title, 'Test Page 1')

    def test_content_items_created(self):
        """
        content items creation test
        """
        audio_found = Audio.objects.get(title='audio 1')
        video_found = Video.objects.get(title='video 1')
        text_found = Text.objects.get(title='text 1')

        self.assertEqual(audio_found.bitrate, 100)
        self.assertEqual(video_found.video_file, 'video1.mkv')
        self.assertEqual(text_found.content, 'Long text content')

    def test_filled_page_created(self):
        """
        page with content items creation test
        """
        page_found = Page.objects.get(title='Test Page 2')

        self.assertEqual(len(page_found.items.all()), 3)


class PageApiTest(APITestCase):
    """
    API Tests
    """

    def setUp(self) -> None:
        audio_item = Audio.objects.create(title='audio 1', bitrate=100)
        video_item = Video.objects.create(title='video 1', video_file='video1.mkv', srt_file='srt.srt')
        text_item = Text.objects.create(title='text 1', content='Long text content')

        page = Page.objects.create(title='API Page 1')
        page.items.set([audio_item,
                        video_item,
                        text_item])

        page2 = Page.objects.create(title='API Page 2')
        page2.items.set([video_item,
                         text_item])

        page3 = Page.objects.create(title='API Page 3')
        page3.items.set([video_item])

    def test_pages_list(self):
        """
        pages list API test
        :return:
        """

        url = reverse('page-list')
        response = self.client.get(url, format='json')

        self.maxDiff = None
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Page.objects.count(), 3)
        self.assertEqual(json.loads(response.content), {'count': 3, 'next': None, 'previous': None, 'results': [
            {'title': 'API Page 1', 'url': 'http://testserver/pages/1/'},
            {'title': 'API Page 2', 'url': 'http://testserver/pages/2/'},
            {'title': 'API Page 3', 'url': 'http://testserver/pages/3/'}]})

    def test_single_page(self):
        """
        single page API test
        :return:
        """

        url = reverse('page-detail', kwargs={'pk': 4})
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'title': 'API Page 1',
                                                        'items': [{'title': 'audio 1', 'bitrate': 100, 'counter': 0},
                                                                  {'title': 'video 1', 'video_file': 'video1.mkv',
                                                                   'srt_file': 'srt.srt', 'counter': 0},
                                                                  {'title': 'text 1', 'content': 'Long text content',
                                                                   'counter': 0}]})
