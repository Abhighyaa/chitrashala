from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('web.urls')),
    url(r'^web/', include('web.urls')),
    url(r'^admin/', admin.site.urls),
]