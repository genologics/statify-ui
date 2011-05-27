from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
   url(r'^$', 'reporting.views.index', name='reporting_index'),
)