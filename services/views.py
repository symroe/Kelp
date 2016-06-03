from django.views.generic import TemplateView, ListView, DetailView

from .models import Service

class ServiceListView(ListView):
    model = Service
    template_name = "service_list.html"


class ServiceDetailView(DetailView):
    model = Service
    template_name = "service_detail.html"

