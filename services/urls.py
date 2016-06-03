from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ServiceListView.as_view(), name="service_list"),
    url(r'^add/$', views.ServiceAddView.as_view(), name="add_service"),
    url(r'^service/(?P<pk>[^/]+)$',
        views.ServiceDetailView.as_view(),
        name="service_detail"),
    url(r'^service/(?P<pk>[^/]+)/used_form$',
        views.ServiceDetailUsedFormView.as_view(),
        name="service_used_form_detail"),

    # url(r'^about/$', views.AboutView.as_view(), name="about_view"),
    # url(r'^league_table/$', views.LeagueTables.as_view(), name="league_table"),
    # url(r'^not_covered/$', views.NotCovered.as_view(), name="not_covered_view"),
    # url(r'^no_data_view/$', views.NoData.as_view(), name="no_data_view"),
    # url(r'^ward/(?P<gss>E\d+)$',
    #     views.WardView.as_view(),
    #     name="ward_view"),
]
