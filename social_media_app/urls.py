from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # accounts
    path('accounts/', include('accounts.urls')),  # handles login, logout, signup, profile

    # posts
    path('feed/', include('posts.urls')),  # all feed-related stuff
]

# Redirect root `/` to feed
urlpatterns += [
    path('', lambda request: redirect('feed')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
