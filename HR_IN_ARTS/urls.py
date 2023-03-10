from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = (
        [
            path('admin/', admin.site.urls),
            path('',include('employee.urls')),
            path('',include("inf0_list.urls")),
            path('',include("home.urls")),
            path('',include("staffing.urls")),
            path('',include("Reference_table.urls"))
        ]
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)