from django.conf.urls import url
from rest_framework.routers import DefaultRouter

import stats.views as views

urlpatterns = [
    url(r'^$', views.index, name='stats-index'),
]

# Code to be run once (https://stackoverflow.com/questions/6791911/execute-code-when-django-starts-once-only)