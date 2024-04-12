
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('course/', include('base.urls')),
    path('result/', include('base.urls')),
    path('userregister/', include('base.urls')),
    path('quiz/', include('base.urls')),
    path('profile/', include('base.urls')),
    path('home/', include('base.urls'))
]
