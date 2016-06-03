from django.views.generic import TemplateView, ListView, DetailView

from .models import Service

class ServiceAddView(TemplateView):
    template_name = "add_product.html"


class ServiceListView(ListView):
    model = Service
    template_name = "service_list.html"


class ServiceDetailView(DetailView):
    model = Service
    template_name = "service_detail.html"

class ServiceDetailUsedFormView(DetailView):
    model = Service
    template_name = "service_detail_used_form.html"

