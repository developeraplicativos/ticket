from django.shortcuts import render
from .models import Requests

# Create your views here.
def visualizar(request): 
    return render(request, 'solicitacoes.html')

class ControllRequest:
    @staticmethod
    def visualizar(): 
        result = Requests.listRequests() 
        return result

    def addRequest():
        return None

    def readResquest():
        return None

    def updateRequest():
        return None

    def deleteResquest():
        return None