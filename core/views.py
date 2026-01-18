from django.shortcuts import render
from django.views import View


# Create your views here.
class HomeView(View):
    template_name = "core/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
