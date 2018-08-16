
# -*- coding: utf-8 -*-

import logging
from django.views.generic import TemplateView
from demosp.settings import TEMPLATE_NAME

LOG = logging.getLogger(__name__)


class IndexView(TemplateView):
  template_name = TEMPLATE_NAME

  def get_context_data(self, **kwargs):
    context = super(IndexView, self).get_context_data(**kwargs)
    context['mpass_data'] = self.request.session.get('MPASS_DATA')
    return context


# vim: tabstop=2 expandtab shiftwidth=2 softtabstop=2
