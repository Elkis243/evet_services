from django.contrib import admin
from django.urls import path, include

# Import custom error handlers
from app import error_handlers

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("app.urls")),
]

# Custom error handlers
handler400 = error_handlers.handler400
handler403 = error_handlers.handler403
handler404 = error_handlers.handler404
handler500 = error_handlers.handler500
