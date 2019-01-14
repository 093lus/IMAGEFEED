from django.conf.urls import url
from django.urls import path


from images_feed import views
from rest_framework import routers

# router = routers.SimpleRouter()
# router.register(r'feed', views.FeedsViewSet)

urlpatterns = [
url(r'feed/', views.FeedsViewSet.as_view()),
]

# urlpatterns += router.urls
