from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ecom_app.urls')),
]+ static(settings.IMAGE_URL, document_root = settings.IMAGE_ROOT)

handler404 = 'ecom_app.views.custom_page_not_found'
