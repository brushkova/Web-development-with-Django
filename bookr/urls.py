from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
import bookr.views
import reviews.views

urlpatterns = [
    path('accounts/', include(('django.contrib.auth.urls', 'auth'), namespace='accounts')),
    path('accounts/profile/', bookr.views.profile, name='profile'),
    path('admin/', admin.site.urls),
    path('', reviews.views.index),
    path('book-search/', reviews.views.BookSearchList.as_view(), name='book_search'),
    path('', include('reviews.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

