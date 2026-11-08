"""Module providing the Application views for Bathynomus"""

from django.shortcuts import render
from django.views import View


class ApplicationView(View):
    """Class handing crud for ApplicationView"""

    @staticmethod
    def get(request, _=None):
        return render(request, "Bathynomus/application.html")
