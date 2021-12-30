from django.shortcuts import render

from django.views import View

class Home(View):
    def get(self, request):
        # stuff
        return render(request, 'gallery/home.html', {})
