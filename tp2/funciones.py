def protocolo_inicio():
    print(" - Bienvenido - ")
    print()


def calcular_combustible(carga_base, reserva=50):
    return carga_base + reserva


def chequeo_sistema(nombre_componente, nivel_energia):
    if nivel_energia >= 70:
        return f"{nombre_componente}: OPERATIVO"
    else:
        return f"{nombre_componente}: FALLIDO"


def calcular_estadisticas(aprobados, fallidos):
    total = aprobados + fallidos

    if total == 0:
        porcentaje_exito = 0
    else:
        porcentaje_exito = (aprobados * 100) / total

    return total, porcentaje_exito