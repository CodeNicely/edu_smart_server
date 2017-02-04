"""edusmartserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from login.views import login,verify
from subjects.views import file_upload
from splash_screen.views import splash
from welcome.views import welcome
from home.views import home
from threads.views import threading,messaging

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login),
    url(r'^verify/', verify),
    url(r'^upload/', file_upload),
    url(r'^splash_screen/', splash),
    url(r'^welcome/', welcome),
    url(r'^home/', home),
    url(r'^thread/', threading),
        url(r'^message/', messaging),

]

from django.conf import settings
from django.conf.urls.static import static
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
