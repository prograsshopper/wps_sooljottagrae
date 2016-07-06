from django.contrib import messages
from django.contrib.auth import logout
from django.views.generic import View
from django.shortcuts import redirect
from django.core.urlresolvers import reverse


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(
            request,
            messages.SUCCESS,
            "로그아웃이 성공적으로 되었습니다."
        )
        return redirect(reverse("login"))