"""sentimental_analysis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import realworld.views
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$',realworld.views.analysis,name='analysis'),
    url(r'^input',realworld.views.input,name = 'input'),
    url(r'^productanalysis',realworld.views.productanalysis,name = 'product analysis'),
    url(r'^textanalysis',realworld.views.textanalysis,name = 'text analysis'),
    url(r'^audioanalysis',realworld.views.audioanalysis,name = 'audio analysis'),
    url(r'^tweetanalysis',realworld.views.tweetanalysis,name = 'tweet analysis'),
    url(r'^imageanalysis',realworld.views.imageanalysis,name = 'image analysis'),
    url(r'^videoanalysis',realworld.views.videoanalysis,name = 'video analysis'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
