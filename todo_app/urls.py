from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.HomeView.as_view(), name="Home"),
    path('home/', views.HomeView.as_view(), name="Home"),
    path('about/', views.AboutView.as_view(), name="about"),
    path('contract/', views.ContractView.as_view(), name="contract"),
    
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
