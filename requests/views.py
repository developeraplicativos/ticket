from django.shortcuts import render

# Create your views here.
def visualizar(request): 
    return render(request, 'solicitacoes.html')