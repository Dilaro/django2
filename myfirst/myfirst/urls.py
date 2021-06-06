from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('blog/', include('blog.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    
]
