from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.Registration.as_view(), name='register'),
    # path('profile/<slug>/', views.Profile.as_view(), name='profile_url'),
]
