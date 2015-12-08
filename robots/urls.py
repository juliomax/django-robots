try:
    from django.conf.urls import url
except ImportError:
    from django.conf.urls.defaults import url

from . import views

urlpatterns = [
    url(r'^$', views.rules_list, name='robots_rule_list'),
]
