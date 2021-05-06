from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from bookr.views import profile


urlpatterns = [
    path('accounts/', include(('django.contrib.auth.urls', 'auth'),
         namespace='accounts')),
    path('accounts/profile/', profile, name='profile'),
    path('admin/', admin.site.urls),
    path('', include('reviews.urls'))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
