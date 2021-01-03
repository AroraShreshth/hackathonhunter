from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class SwaggerUI(LoginRequiredMixin, TemplateView):
    template_name = 'swagger-ui.html'
    extra_context = {'schema_url': 'openapi-schema'}


class ReDocUI(LoginRequiredMixin, TemplateView):
    template_name = 're-doc.html'
    extra_context = {'schema_url': 'openapi-schema'}
