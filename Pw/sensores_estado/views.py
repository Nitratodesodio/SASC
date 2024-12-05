from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from administracion.models import Controlador,Sala, SalaTipoError



def test(request):
    # Obtener todas las salas
    todas_las_salas = Sala.objects.all()

    # Obtener todas las relaciones de errores con las salas
    errores = SalaTipoError.objects.select_related('sala', 'tipo_error').all()

# Imprimir cada error con su sala y tipo de error
    for error in errores:
        print(f"Sala: {error.sala.sala}, Tipo de Error: {error.tipo_error.nombre}, Fecha: {error.fecha}")


    # Crear un diccionario de salas por id para un acceso rápido
    salas_dict = {sala.cod_sala: sala for sala in todas_las_salas}
    

    # Inicializar la lista de errores para cada sala
    for sala in todas_las_salas:
        sala.errores = []
    

    # Asociar errores a las salas correspondientes
    for error in errores:
        sala_id = error.sala.cod_sala
        if sala_id in salas_dict:
            salas_dict[sala_id].errores.append(error.tipo_error.nombre)


    # Crear un diccionario para agrupar las salas por piso
    pisos = {
        -1: sorted(
            [sala for sala in todas_las_salas if sala.sala.isdigit() and 1 <= int(sala.sala) <= 99],
            key=lambda sala: int(sala.sala)
        ),
        1: sorted(
            [sala for sala in todas_las_salas if sala.sala.isdigit() and 100 <= int(sala.sala) <= 199],
            key=lambda sala: int(sala.sala)
        ),
        2: sorted(
            [sala for sala in todas_las_salas if sala.sala.isdigit() and 200 <= int(sala.sala) <= 299],
            key=lambda sala: int(sala.sala)
        ),
        3: sorted(
            [sala for sala in todas_las_salas if sala.sala.isdigit() and 300 <= int(sala.sala) <= 399],
            key=lambda sala: int(sala.sala)
        ),
        4: sorted(
            [sala for sala in todas_las_salas if sala.sala.isdigit() and 400 <= int(sala.sala) <= 499],
            key=lambda sala: int(sala.sala)
        ),
        5: sorted(
            [sala for sala in todas_las_salas if sala.sala.isdigit() and 500 <= int(sala.sala) <= 599],
            key=lambda sala: int(sala.sala)
        ),
    }

    # Pasar el contexto al template
    context = {
        'pisos': pisos,
        'errores': errores,  # Lista de errores para la barra de notificaciones
    }
    return render(request, 'test.html', context)



