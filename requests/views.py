from django.shortcuts import render
from abc import ABC, abstractmethod
from .models import Requests

# Create your views here.
def visualizar(request): 
    return render(request, 'solicitacoes.html')

class ControllRequestInternal(ABC):
    # @staticmethod
    # def visualizar(): 
    #     result = Requests.listRequests() 
    #     return result 

    @staticmethod
    def visualizar():
        result = Requests.listRequests() 
        return result 

    @staticmethod
    def addRequest(about, title):
        result = Requests.addRequest(about, title)
        return result 

    @staticmethod
    def readResquest(id):
        result = Requests.readRequest(about, title)
        return result 

    @staticmethod
    def updateRequest(about, title,id):
        result = Requests.updateRequest(about, title, id)
        return result 

    @staticmethod
    def deleteResquest(id):
        result = Requests.deleteteRequest( id)
        return result 