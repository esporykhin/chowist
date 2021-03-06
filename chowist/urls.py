"""chowist URL Configuration

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
from django.urls import path, include

# Default app
urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
]

# Custom apps
apps = [{"entry": "", "name": "portal"}, {"entry": "places/", "name": "places"}]


def get_app_path(app):
    """Get application path for urlpatterns.

    https://docs.djangoproject.com/en/3.0/ref/urls/#include

    Args:
        app: Application instance.

    Returns:
        Application path instance.
    """
    app_entry = app["entry"]
    app_name = app["name"]
    app_urls = app_name + ".urls"
    return path(app_entry, include((app_urls, app_name), namespace=app_name))


for app in apps:
    urlpatterns.append(get_app_path(app))
