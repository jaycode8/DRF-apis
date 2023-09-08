
from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from jaymoh import settings

urlpatterns = [
    re_path("books", views.book_view),
    re_path("book/", views.book_view2),
    re_path("authors", views.author_view),
    re_path("author/", views.author_view2),
    re_path("test", views.test),
    re_path("", views.home, name='home route')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
