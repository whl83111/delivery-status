from django.shortcuts import render
import getStatus.getDeliveryData as getData
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def index(request):
	return render(request, 'index.html')

@csrf_protect
def getDeliveryStatus(request):
	deliveryId = request.POST
	DongPoo = getData.getDongPoo(deliveryId)
	BlackCat = getData.getBlackCat(deliveryId)
	result = {'DongPoo' : DongPoo, 'BlackCat' : BlackCat}
	return JsonResponse(result)