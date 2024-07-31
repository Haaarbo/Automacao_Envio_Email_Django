from django.http import HttpResponse

#def resposta ao ser enviado o e-mail
def index(request):
    return HttpResponse('E-mail enviado com sucesso!')
