from django.views.generic import TemplateView
from .coretools import AdminStaffRequiredMixin


class SwaggerUI(AdminStaffRequiredMixin, TemplateView):
    template_name = 'swagger-ui.html'
    extra_context = {'schema_url': 'openapi-schema'}

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


class ReDocUI(AdminStaffRequiredMixin, TemplateView):
    template_name = 're-doc.html'
    extra_context = {'schema_url': 'openapi-schema'}

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff
