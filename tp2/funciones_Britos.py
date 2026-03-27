def protocolo_inicio():
    print(" - Bienvenido - ")
    print()


def calcular_combustible(carga_base, reserva=50):
    total = carga_base + reserva
    return total


def chequeo_sistema(nombre, nivel):
    if nivel >= 70:
        return nombre + ": OPERATIVO"
    else:
        return nombre + ": FALLIDO"


def calcular_estadisticas(aprobados, fallidos):
    total = aprobados + fallidos
    porcentaje = (aprobados * 100) / total
    return total, porcentaje