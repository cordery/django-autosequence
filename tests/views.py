from django.db import IntegrityError
from django.http import HttpResponse
from django.views import View

from autosequence.helpers import lock_table
from tests.models import SimpleModel


class TestLockedTableRaceView(View):
    http_method_names = ['post']

    def post(self, request, **kwargs):
        with lock_table(SimpleModel):
            SimpleModel.objects.create()
        return HttpResponse(status=200)


class TestNoLockRaceView(View):
    http_method_names = ['post']

    def post(self, request, **kwargs):
        try:
            SimpleModel.objects.create()
        except IntegrityError:
            pass
        return HttpResponse(status=200)
