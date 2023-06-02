from django.urls import path, include
from django.contrib import admin


from . import views

urlpatterns = [
    path('', views.home_view),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
]
