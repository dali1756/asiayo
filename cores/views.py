from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from django.views import View
import json
from django.http import HttpResponse

@method_decorator(require_http_methods(["POST"]), name='dispatch')
class OrderView(View):
    def post(self, request):
        data = {
            "id": request.POST.get("id", ""),
            "name": request.POST.get("name", ""),
            "address": {
                "city": request.POST.get("city", ""),
                "district": request.POST.get("district", ""),
                "street": request.POST.get("street", "")
            },
            "price": request.POST.get("price", ""),
            "currency": request.POST.get("currency", "")
        }
        
        if all(data.values()):
            return render(request, "order.html", {"data": data})
        else:
            return HttpResponse("缺少必要的字段", status=400)
def order_form(request):
    return render(request, "order_form.html")