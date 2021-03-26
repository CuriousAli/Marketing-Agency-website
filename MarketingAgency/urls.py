from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from MarketingAgency import settings
from advertising.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('advertising.urls'))
]

'''That condition ONLY for debug mode'''
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = pageNotFound