from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mainapp.views.home', name='home'),
    # url(r'^mainapp/', include('mainapp.foo.urls')),

    url(r'^scan/$', 'receipts.views.scan'),
    url(r'^scan/sms/$', 'receipts.views.scan_sms'),
    url(r'^remind/$', 'receipts.views.remind', name='remind'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
