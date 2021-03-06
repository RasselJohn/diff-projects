import json
from typing import Optional

from django.http import JsonResponse, HttpRequest
from django.utils.translation import gettext_lazy as _
from django.views import View

from src.apps.api.forms import DomainsAddForm
from src.apps.api.utils import get_form_errors


class DomainsAddView(View):
    def post(self, request: HttpRequest) -> JsonResponse:
        form = DomainsAddForm(json.loads(request.body))
        if not form.is_valid():
            return JsonResponse(get_form_errors(form), status=400)

        timestamp: Optional[float] = form.save_urls()
        if timestamp is None:
            return JsonResponse({'status': _('Ошибка сервера. Пожалуйста, обратитесь позже.')}, status=502)

        return JsonResponse({
            'timestamp': timestamp,  # need for testing
            'status': 'ok'
        })
