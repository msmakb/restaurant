from django.shortcuts import render, redirect

from django.http import HttpRequest, HttpResponse

from . import constants


def index(request: HttpRequest) -> HttpResponse:

    return render(request, constants.TEMPLATES.INDEX_PAGE_TEMPLATE, {'r': range(20)})
