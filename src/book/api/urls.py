from django.conf.urls import url

from .views import BookListAPIView,BookUpdateDeleteRetrieveAPIView
urlpatterns = [
	url(r'^$',BookListAPIView.as_view()),
	url(r'^(?P<id>\d+)/$',BookUpdateDeleteRetrieveAPIView.as_view()),
]