from django.contrib.auth.models import User
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View


class UserRemoveView(View):
    template_name = 'user-remove.html'

    def get(self, request: HttpRequest, user_id: str) -> HttpResponse:
        return render(request, self.template_name, {'user_id': user_id})

    def post(self, request: HttpRequest, user_id: str) -> JsonResponse:
        user: User = get_object_or_404(User, pk=user_id)

        # don't remove! just switch off
        user.is_active = False
        user.save(update_fields=['is_active'])

        return JsonResponse({'url': reverse_lazy('users')})
