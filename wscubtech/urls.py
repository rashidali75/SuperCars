from unicodedata import name
from django.contrib import admin
from django.urls import path
from wscubtech import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('about', views.about,name='about'),
    path('services', views.services,name='services'),
    path('contact', views.contact,name='contact'),

# cars app start operation
    # path('cars',views.cars,name='cars')

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
