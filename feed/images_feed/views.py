from django.conf.global_settings import MEDIA_URL
from django.core.files.storage import FileSystemStorage
from rest_framework import viewsets, generics, mixins
from rest_framework.exceptions import NotFound
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework import status
from images_feed.models import Feed
from images_feed.serilalizers import FeedListSerializer

from feed.settings import MEDIA_ROOT




class FeedListPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    invalid_page_message = 'NO MORE IMAGES'

    def paginate_queryset(self, queryset, request, view=None):
        """Checking NotFound exception"""
        try:
            return super(FeedListPagination, self).paginate_queryset(queryset, request, view=view)
        except NotFound:
            return []


class FeedsViewSet(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Feed.objects.all()
    serializer_class = FeedListSerializer
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('file')
        location = '{}/photos'.format(MEDIA_ROOT)
        fs = FileSystemStorage(location=location, base_url='{}/photos'.format(MEDIA_URL))
        filename = fs.save(image.name, image)
        uploaded_file_url = fs.url(filename)
        feed = Feed(title=title, description=description, image = uploaded_file_url)
        feed.save()
        return Response(status=status.HTTP_200_OK)

    def get(self, request):
        queryset = self.get_queryset()
        page = FeedListPagination()
        partial_queryset = page.paginate_queryset(queryset, request)
        serializer = FeedListSerializer(partial_queryset, many=True)
        return Response(serializer.data)


    def put(self, request ):
        pk = request.POST.get('id')
        feed = Feed.objects.get(pk=pk)
        feed.status = not feed.status
        feed.save()
        return Response(status=status.HTTP_200_OK)
