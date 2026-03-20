from django.http import HttpResponse

def home(request):
    return HttpResponse("Sistema de eventos funcionando!")