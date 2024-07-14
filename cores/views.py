from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from django.views import View
import json
from django.http import HttpResponse
from .forms import OrderForm

@method_decorator(require_http_methods(["POST"]), name='dispatch')
class OrderView(View):
    def post(self, request):
        form = OrderForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if data["currency"] == "USD":
                data["price"] *= 31
                data["currency"] = "TWD" 
            return JsonResponse(data)
        else:
            return JsonResponse({"errors": form.errors}, status=400)
        
def order_form(request):
    return render(request, "order_form.html")