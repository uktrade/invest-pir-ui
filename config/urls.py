"""pir_frontend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from pir_frontend.views import PIRView, ProxyView, succes_view

urlpatterns = [
    url('^$', PIRView.as_view(), name='pir_view_root'),
    url('^reports/(?P<filename>.*)$', ProxyView.as_view()),
    url('^perfectfit/reports/(?P<filename>.*)$', ProxyView.as_view()),
    url('^perfectfit/$', PIRView.as_view(), name='pir_view'),
    url(
        '^perfectfit/success/$', succes_view,
        name='pir_view_success'
    ),
]
