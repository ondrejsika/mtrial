if DEBUG:
    urlpatterns += patterns('',
        url(r'^static/uploads/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': MEDIA_ROOT,
        }), 
        url(r'^static/static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': STATIC_ROOT,
        }), 
   ) 

if ADMIN_URLS:
    from django.contrib import admin

    admin.autodiscover()
    urlpatterns += patterns('', 
        url(r'^admin/', include(admin.site.urls)),
    )
