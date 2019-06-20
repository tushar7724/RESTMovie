from django.conf.urls import url, include
from django.contrib import admin
from .api import router

urlpatterns = [
    ############ Admin url to make all CRUD operations ############
    url(r'^admin/', admin.site.urls),

    ############ Normal Users url for only API View access ############
    url('api/', include(router.urls)),
]