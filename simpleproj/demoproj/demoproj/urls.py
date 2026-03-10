from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('movies/', include('movies.urls')),  # your app
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/movies/', permanent=False)),  # redirect root
]