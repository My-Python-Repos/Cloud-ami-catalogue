from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^make_update', views.make_update, name='update'),
    url(r'^make_ami', views.make_ami, name='ami'),
    # /ami_info
    url(r'^$', views.index, name='index'),
    # /ami_info/ami-4ddcf436
    url(r'^(?P<ami_id_used>ami-[a-z0-9]{8})/$', views.detail, name='detail'),
]
