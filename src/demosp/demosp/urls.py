
# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from demosp.views import IndexView

urlpatterns = [
  url(r'^$', login_required()(IndexView.as_view()),
    name='demosp_index'),
]


# vim: tabstop=2 expandtab shiftwidth=2 softtabstop=2
