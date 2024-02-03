from django.contrib import admin
from django.urls import path, include
from myapp.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    # path('__debug__/', include("debug_toolbar.urls")),
]
