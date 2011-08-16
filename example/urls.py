from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import dynamic_rules
dynamic_rules.autodiscover()

urlpatterns = patterns('',
    # url(r'^admin/', include(admin.site.urls)),
)
