from django.http import HttpResponse
from rest_framework.views import APIView

from utils.api.crwal import Crawler


class CrawlerView(APIView):
    def post(self, request):
        result = Crawler(request.POST.get('url'))
        data = result.parse()
        return HttpResponse(data, content_type='application/json')

    def get(self, request):
        data = Crawler().parse()
        return HttpResponse(data, content_type='application/json')


