from django.views.generic import View 
from django.shortcuts import render

class DashboardView(View):
    def get(self, request, *args, **kwargs):
        context={

        }
        return render(request, 'dashboard.html', context)

class InformeView(View):
    def get(self, request, *args, **kwargs):
        context={

        }
        return render(request, 'informes.html', context)

class AlertaView(View):
    def get(self, request, *args, **kwargs):
        context={

        }
        return render(request, 'alertas.html', context)