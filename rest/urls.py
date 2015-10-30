from django.conf.urls import url

from views import CrawlerView


urlpatterns = [
    url(r'crawl/url/$', CrawlerView.as_view(), name='base'),
]
