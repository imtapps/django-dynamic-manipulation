from django.conf.urls.defaults import patterns
from django.contrib import admin
import dynamic_rules

admin.autodiscover()
dynamic_rules.autodiscover()
urlpatterns = patterns('', )
