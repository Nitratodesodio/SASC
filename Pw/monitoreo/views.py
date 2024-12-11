from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from administracion.models import Controlador,Sala, SalaTipoError, Lectura,Sensor,EstadoAc
from datetime import date, datetime, timedelta

@login_required()
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required()
def informes(request):
    return render(request, 'informes.html')

@login_required()
def alertas(request):
   # # Obtener la fecha de hoy
   #  hoy = date.today()
   #
   #  # Obtener todas las salas
   #  todas_las_salas = Sala.objects.all()
   #
   #  # Obtener las relaciones de errores con las salas, filtrando por fecha de hoy
   #  errores = SalaTipoError.objects.all().filter(fecha__date=hoy)
   #
   #  # Crear un diccionario de salas por ID
   #  salas_dict = {sala.cod_sala: (sala,[]) for sala in todas_las_salas}
   #
   #  # Inicializar la lista de errores y el estado para cada sala
   #  for sala in todas_las_salas:
   #      sala.errores = []
   #      sala.estado = 'Inactivo'  # Estado predeterminado
   #
   #  # Asociar errores a las salas correspondientes
   #  for error in errores:
   #      sala_id = error.sala.cod_sala
   #      if sala_id in salas_dict:
   #          salas_dict[sala_id].errores.append(error.tipo_error.nombre)
   #
   #  # Verificar actividad de sensores
   #  tiempo_limite = datetime.now() - timedelta(minutes=15)  # Sensores activos en los últimos 15 minutos
   #  lecturas_recientes = Lectura.objects.filter(fecha_hora__gte=tiempo_limite).select_related('cod_sensor')
   #  sensores_activos = {
   #      lectura.cod_sensor.cod_controlador.cod_controlador
   #      for lectura in lecturas_recientes
   #      if lectura.cod_sensor and lectura.cod_sensor.cod_controlador
   #  }
   #
   #
   #  # Actualizar el estado de las salas según errores y sensores activos
   #  for sala in todas_las_salas:
   #      sala.estado = 'Inactivo'  # Estado predeterminado
   #      if sala.errores:  # Si tiene errores
   #          sala.estado = 'Con errores'
   #      elif sala.cod_controlador and sala.cod_controlador.cod_controlador in sensores_activos:
   #          sala.estado = 'Activo'
   #
   #  # Crear un diccionario para agrupar las salas por piso
   #  pisos = {
   #      -1: sorted(
   #          [sala for sala in todas_las_salas if sala.sala.isdigit() and 1 <= int(sala.sala) <= 99],
   #          key=lambda sala: int(sala.sala)
   #      ),
   #      1: sorted(
   #          [sala for sala in todas_las_salas if sala.sala.isdigit() and 100 <= int(sala.sala) <= 199],
   #          key=lambda sala: int(sala.sala)
   #      ),
   #      2: sorted(
   #          [sala for sala in todas_las_salas if sala.sala.isdigit() and 200 <= int(sala.sala) <= 299],
   #          key=lambda sala: int(sala.sala)
   #      ),
   #      3: sorted(
   #          [sala for sala in todas_las_salas if sala.sala.isdigit() and 300 <= int(sala.sala) <= 399],
   #          key=lambda sala: int(sala.sala)
   #      ),
   #      4: sorted(
   #          [sala for sala in todas_las_salas if sala.sala.isdigit() and 400 <= int(sala.sala) <= 499],
   #          key=lambda sala: int(sala.sala)
   #      ),
   #      5: sorted(
   #          [sala for sala in todas_las_salas if sala.sala.isdigit() and 500 <= int(sala.sala) <= 599],
   #          key=lambda sala: int(sala.sala)
   #      ),
   #  }
   #
   #  # Salas no clasificadas
   #  salas_no_clasificadas = [
   #      sala for sala in todas_las_salas if not sala.sala.isdigit()
   #  ]

    # Pasar el contexto al template
    # context = {
    #     'pisos': pisos,
    #     'salas_no_clasificadas': salas_no_clasificadas,
    #     'errores': errores,  # Lista de errores para la barra de notificaciones
    # }
    #temperaturas_altas = Lectura.objects.filter(cod_sensor=2).filter(models.Q(valor__lt=21) | models.Q(valor__gt=25))
    alertas = SalaTipoError.objects.all().order_by('-fecha')
    context = {
        'alertas': alertas
    }
    return render(request, 'alertas.html', context)