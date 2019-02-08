from django.conf.urls import url

from .views import BookList,BookRUDAPIView,CRUDLAPIView

urlpatterns = [
	url(r'^$',BookList.as_view()),
	url(r'^(?P<id>\d+)/$',BookRUDAPIView.as_view()),
]