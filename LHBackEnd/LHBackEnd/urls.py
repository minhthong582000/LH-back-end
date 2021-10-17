"""LHBackEnd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view

# swagger documentation
schema_swagger_view = get_swagger_view(title='Recipes API')
# coreapi documentation
schema_view = get_schema_view(title="Recipes API")

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^auth/', include('authentication.urls', namespace='authentication')),
    url(r'^api/', include(('menu.urls'), namespace='menu')),
    # rest_framework urls for session authentication for the browsable api
    #url(r'^api-auth/', include('rest_framework.urls')),
    url(r'api_docs/', schema_swagger_view),
    url(r'docs/', include_docs_urls(title='Recipes API')),
    url(r'schema', schema_view),
]

