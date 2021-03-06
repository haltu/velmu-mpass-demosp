
# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin

class AdminSite(admin.AdminSite):
  def has_permission(self, request):
    return request.user.is_active and request.user.is_staff and request.user.is_superuser

admin.site = AdminSite()
admin.autodiscover()


admin_urls = [
  url(r'^sysadmin/', include(admin.site.urls)),
]

app_urls = [
  url(r'^login/saml/', include('mpass.urls.login')),
  url(r'^', include('demosp.urls')),
]

auth_urls = [
  url(r'^', include('django.contrib.auth.urls')),
]

static_urls = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
static_urls += staticfiles_urlpatterns()

urlpatterns = admin_urls + app_urls + static_urls + auth_urls


# vim: tabstop=2 expandtab shiftwidth=2 softtabstop=2

