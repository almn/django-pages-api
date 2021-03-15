from celery import shared_task

from app.models import Page, ContentItem


@shared_task
def increase_page_counters(page_id: int):
    page = Page.objects.get(pk=page_id)
    if page:
        page_items = page.items.all()
        for page_item in page_items:
            if isinstance(page_item, ContentItem):
                page_item.increase_counter()
