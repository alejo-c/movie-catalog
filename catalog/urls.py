from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("catalog", views.catalog, name="catalog"),
    path("catalog/add", views.add, name="add"),
    path("catalog/view/<int:movie_id>", views.view, name="view"),
    path("catalog/edit/<int:movie_id>", views.edit, name="edit"),
    path("catalog/remove/<int:movie_id>", views.remove, name="remove"),
    path("logout/", views.logout_view, name="logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
