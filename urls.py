from django.conf.urls.defaults import *
from mysite.views import zhuye,hello,lianxi,liuyan,liuyanold
from django.views.generic.simple import direct_to_template
from mysite import settings
from django.template import Template,Context,TemplateDoesNotExist
from django.template.loader import get_template as get_Template
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
   (r'^$',zhuye),
   (r'^liuyan.html$',liuyan),
   (r'^lianxi.html$',lianxi),
   (r'^liuyanold.html$',liuyanold),
   (r'^jianjie.html$',direct_to_template,{'template':'jianjie.html'}),
   (r'^site_media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_PATH}),
    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),
    (r'^admin/',include(admin.site.urls)),
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
