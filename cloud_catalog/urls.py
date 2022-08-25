from django.conf.urls import include, url
from django.contrib import admin



urlpatterns = [
    
    url(r'^make_ami/', include('ami_info.urls')),
    url(r'^make_update/', include('ami_info.urls')),
    url(r'^ami_info/', include('ami_info.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'', include('onboard.urls')),
]
