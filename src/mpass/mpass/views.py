# -*- coding: utf-8 -*-
#
# Copyright Haltu Oy, info@haltu.fi
# All rights reserved.
#


import logging
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, authenticate, get_user_model, login as auth_login,
    update_session_auth_hash,
)
from django.contrib.auth.views import SuccessURLAllowedHostsMixin
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseRedirect
from django.shortcuts import resolve_url
from django.utils.decorators import method_decorator
from django.utils.http import is_safe_url
from django.utils.translation import get_language_from_request
from django.views.decorators.cache import never_cache
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import TemplateView
from mpass.models import AuthenticationSource
from mpass import settings


LOG = logging.getLogger(__name__)


class MPASSLoginView(SuccessURLAllowedHostsMixin, TemplateView):
  """
  Display the login method selection page and handle the login action.
  """
  redirect_field_name = REDIRECT_FIELD_NAME
  template_name = 'mpass/auth_method_selection.html'
  redirect_authenticated_user = False
  extra_context = None

  @method_decorator(sensitive_post_parameters())
  @method_decorator(never_cache)
  def dispatch(self, request, *args, **kwargs):
    if self.redirect_authenticated_user and self.request.user.is_authenticated:
      redirect_to = self.get_success_url()
      if redirect_to == self.request.path:
        raise ValueError(
          "Redirection loop for authenticated user detected. Check that "
          "your LOGIN_REDIRECT_URL doesn't point to a login page."
        )
      return HttpResponseRedirect(redirect_to)
    return super(MPASSLoginView, self).dispatch(request, *args, **kwargs)

  def get(self, request, *args, **kwargs):
    user = authenticate(request_meta=request.META)
    if user:
      # Okay, security check complete. Log the user in.
      auth_login(request, user)
      self.save_mpass_data_to_session(request)
      return HttpResponseRedirect(self.get_success_url())
    else:
      LOG.info('Could not authenticate user from the headers')
      return super(MPASSLoginView, self).get(request, *args, **kwargs)

  def get_success_url(self):
      url = self.get_redirect_url()
      return url or resolve_url(settings.LOGIN_REDIRECT_URL)

  def get_redirect_url(self):
      """Return the user-originating redirect URL if it's safe."""
      redirect_to = self.request.POST.get(
          self.redirect_field_name,
          self.request.GET.get(self.redirect_field_name, '')
      )
      url_is_safe = is_safe_url(
          url=redirect_to,
          allowed_hosts=self.get_success_url_allowed_hosts(),
          require_https=self.request.is_secure(),
      )
      return redirect_to if url_is_safe else ''

  def get_context_data(self, **kwargs):
      context = super(MPASSLoginView, self).get_context_data(**kwargs)
      lang = get_language_from_request(self.request)
      print(lang)
      auth_sources = AuthenticationSource.objects.active_translations(lang).order_by('translations__title').distinct()
      current_site = get_current_site(self.request)
      context.update({
          self.redirect_field_name: self.get_redirect_url(),
          'site': current_site,
          'site_name': current_site.name,
          'auth_sources': auth_sources,
      })
      if self.extra_context is not None:
        context.update(self.extra_context)
      return context

  def save_mpass_data_to_session(self, request):
    mpass_data = {}
    keys = [
      'HTTP_MPASS_CLASS',
      'HTTP_MPASS_CLASSLEVEL',
      'HTTP_MPASS_CURRENTGIVENNAME',
      'HTTP_MPASS_GIVENNAME',
      'HTTP_MPASS_LEGACYCRYPTID',
      'HTTP_MPASS_LEGACYCRYPTIDE',
      'HTTP_MPASS_MUNICIPALITY',
      'HTTP_MPASS_MUNICIPALITYCODE',
      'HTTP_MPASS_ROLE',
      'HTTP_MPASS_SCHOOL',
      'HTTP_MPASS_SCHOOLCODE',
      'HTTP_MPASS_SN',
      'HTTP_MPASS_UID',
    ]
    for k in keys:
      value = request.META.get(k, None)
      if value is not None:
        value = unicode(value.decode('utf-8'))
      mpass_data[k] = value
    request.session['MPASS_DATA'] = mpass_data

# vim: tabstop=2 expandtab shiftwidth=2 softtabstop=2

