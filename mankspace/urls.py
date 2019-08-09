from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')), 
    path('accounts/', include('accounts.urls')), # First will look if it is logged in and then it will proceed to the account app
    path('admin/', admin.site.urls),
    path('posts', include('post.urls')), # Linking this with post app 
    path('', include('post.urls')), # Linking this with post app 
]
