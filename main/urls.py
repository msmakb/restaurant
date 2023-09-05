from django.urls import path

from . import views
from .constants import PATH


urlpatterns = [
    path('', views.index, name=PATH.INDEX_PAGE),
]
