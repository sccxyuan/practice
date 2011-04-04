from django.conf.urls.defaults import *
#from mysite.views import zhuye,hello,lianxi,liuyan,liuyanold,mendian,houqing,shop_detail
from mysite import views
from django.views.generic.simple import direct_to_template
from mysite import settings
from django.views.generic import list_detail
from django.template import Template,Context,TemplateDoesNotExist
from django.template.loader import get_template as get_Template
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('mysite.views',
   (r'^$','zhuye'),
   (r'^mendian.html$','mendian'),
   (r'^liuyan.html$','liuyan'),
   (r'^houqing.html$','houqing'),
   (r'^lianxi.html$','lianxi'),
   (r'^liuyanold.html$','liuyanold'),
   (r"^guanli.html$",direct_to_template,{'template':'guanli.html'}),
   (r"^jiameng.html$",direct_to_template,{'template':'jiameng.html'}),
   (r"^qiyewenhua.html$",direct_to_template,{'template':'qiyewenhua.html'}),
   (r'^jianjie.html$',direct_to_template,{'template':'jianjie.html'}),
   #(r'^shop/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_PATH})
  # 
    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r"^shop/(?P<shop_id>\d+)/$",'shop_detail'),
    (r"^news/(?P<new_id>\d+)/$",'news'),
    (r"^article/(?P<article_id>\d+)/$",'article'),
    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
urlpatterns += patterns('',
    (r'^admin/',include(admin.site.urls)),
    (r'^site_media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_PATH}),
    )