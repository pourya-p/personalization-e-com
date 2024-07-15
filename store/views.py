from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, requests):
        return render(requests, 'store/index.html')
