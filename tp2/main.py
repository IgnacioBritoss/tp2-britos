from funciones import protocolo_inicio, calcular_combustible, chequeo_sistema, calcular_estadisticas
protocolo_inicio()

capitan = input("Ingrese el nombre del capitan/a: ")
print()

cantidad_sistemas = int(input("Cuantos sistemas se van a inspeccionar?: "))
print()
aprobados = 0
fallidos = 0
contador = 1

while contador <= cantidad_sistemas:
    print("Sistema", contador)

    nombre_sistema = input("Nombre del sistema: ")

    nivel_energia = int(input("Nivel de energia (0 a 100): "))
    while nivel_energia < 0 or nivel_energia > 100:
        print("Error: el nivel de energia debe estar entre 0 y 100.")
        nivel_energia = int(input("Ingrese nuevamente el nivel de energia: "))

    resultado = chequeo_sistema(nombre_sistema, nivel_energia)
    print("Resultado:", resultado)

    if nivel_energia >= 70:
        aprobados += 1
    else:
        fallidos += 1

    print()
    contador += 1

carga_base = int(input("Ingrese la carga base de combustible: "))
combustible_total = calcular_combustible(carga_base)

print()
print("Combustible total:", combustible_total)
print()

total_sistemas, porcentaje_exito = calcular_estadisticas(aprobados, fallidos)
print("REPORTE FINAL")
print("Capitan/a:", capitan)
print("Total de sistemas revisados:", total_sistemas)
print("Sistemas operativos:", aprobados)
print("Sistemas fallidos:", fallidos)
print("Porcentaje de exito:", porcentaje_exito, "%")
print("Fin de la verificacion.")