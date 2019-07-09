from django.conf.urls import url, include
from django.contrib import admin
from .views import home_redirect

urlpatterns = [
    url(r'^$', home_redirect, name='home_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^book/', include(('books.urls', 'books'), namespace='books')),
]
