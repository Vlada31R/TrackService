from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    path('accounts/', include('accounts.urls')),
    path('tracks/', include('tracks.urls')),
)
urlpatterns += [
    path('', RedirectView.as_view(url='tracks/'))
]
