from django.http import HttpResponse
from django.core.mail import EmailMessage, send_mail, EmailMultiAlternatives #classe que permite envio de e-mail
from django.template.loader import render_to_string #

#def resposta ao ser enviado o e-mail
def index(request):
    context = { "name": "Abrahão" }
    html_content = render_to_string('mail/test-mail.html', context)
    plain_context = render_to_string('mail/test-mail.txt', context)
    #forma 1 de settar dados do e-mail, puxando uma classe e criando um objeto para envio do e-mail
    #mail = EmailMessage(
    #    subject='E-mail teste',
    #    body='Teste de envio de e-mail automático usando django',
    #    from_email='abrahao0707@gmail.com',
    #    to=['abrahao0707@gmail.com'],
    #)
    #mail.send()
    
    #forma 2 de settar dados do e-amil, ja importando a funcao que ja puxara os mesmo atributos
    # send_mail(
    #     subject='E-mail teste',
    #     #message quando se envia texto sem formatacao
    #     message=plain_context,
    #     from_email='abrahao0707@gmail.com',
    #     recipient_list=['abrahao0707@gmail.com'],
    #     #html_message para mandar conteudo de string com template de formatacao
    #     html_message=html_content
    # )

    mail = EmailMultiAlternatives(
        subject='E-mail teste',
        body=plain_context,
        from_email='abrahao0707@gmail.com',
        to=['abrahao0707@gmail.com'],
    )
    mail.attach_alternative(html_content, 'text/html')
    mail.attach_file('mail/midia/anexo.txt')
    mail.send()

    return HttpResponse('E-mail enviado com sucesso!')
