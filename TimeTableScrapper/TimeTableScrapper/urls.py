
from django.conf.urls import include, url
from django.contrib import admin
from scrap.views import getcaptcha,postdata
from django.conf.urls.static import static
#from TimeTableScrapper import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^getdata/$',getcaptcha,name='getcaptcha'),
    url(r'^postdata/$',postdata,name='postdata'),
]
#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
