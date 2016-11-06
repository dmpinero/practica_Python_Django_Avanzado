from django.shortcuts import render, redirect


def autorizarAcceso(request, client_id):
    redireccion = "http://127.0.0.1:8000/oauth/authorize?response_type=code&client_id=" + client_id + "&redirect_url=http://127.0.0.1:8000/terceros/obtenerAuthCode"

    response = redirect(redireccion)
    return render(request, 'integracion_terceros/permitir_autorizacion.html')

def obtenerAuthCode(request):
    return render(request, 'integracion_terceros/resultado.html')
