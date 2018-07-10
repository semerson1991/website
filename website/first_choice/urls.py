from django.conf.urls import url, include
from . import views
from first_choice.views import ImagesListView
from first_choice.views import PortfolioView

from django.views.generic import ListView, DetailView
from first_choice.models import Video, Image



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/', views.contact, name='contact'),
   # url(r'^portfolio/', ListView.as_view(queryset=Image.objects.all(), template_name="personal/portfolio.html")),
url(r'^portfolio/', PortfolioView.as_view(), name='portfolio_list'),
#url(r'^portfolio/', ListView.as_view(queryset=Image.objects.all(), template_name='personal/portfolio.html')),
    url(r'^videos/', ListView.as_view(queryset=Video.objects.all(), template_name="personal/videos.html")),
    url(r'^video/(?P<pk>\d+)$', DetailView.as_view(model = Video, template_name = "personal/video.html"))
]