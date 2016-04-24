from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from .models import Company,Feedback

urlpatterns = patterns('',
	url(r'^$', ListView.as_view(
				queryset = Company.objects.all(),
				template_name = "company.html")),

	url(r'^(?P<pk>\d+)$', ListView.as_view(
				model = Feedback,
				template_name = "post.html")),
)