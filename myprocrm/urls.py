
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^mycrm/', include("mycrm.urls")),
    url(r'^student/', include("student.urls")),
    url(r'^superadmin/', include("superadmin.urls")),

]
