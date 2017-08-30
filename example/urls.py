from django.conf.urls.defaults import patterns

from django.contrib import admin
admin.autodiscover()

import dynamic_rules
dynamic_rules.autodiscover()

urlpatterns = patterns('',
                       # url(r'^admin/', include(admin.site.urls)),
                      )
