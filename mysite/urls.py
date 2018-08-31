from django.urls import path, include
from django.contrib import admin
# from django.conf.urls import url, include


urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'blog/', include('blog.urls', namespace='blog')),
]
