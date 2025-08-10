
"""Crear una función llamada procesar_notas(estudiantes) la cual va a recibir
un diccionario donde las claves serán los nombres de los estudiantes y sus
valores serán listas con 3 notas.
- Calcular el promedio de cada estudiantes.
- Devolver un nuevo diccionario donde la clave sea el nombre del estudiante
y el valor sea otro diccionario con:
promedio: que será el promedio de notas
estado: “aprobado” si es mayor o igual a 11, “desaprobado” si es menor
- Mostrar en pantalla el estudiante con mayor promedio"""

dic = {"Armando":[19,15,18], "Mateo": [17,16,20], "Pablo":[20,13,8] }

def media(n: list):
    sum = 0
    for i in n:
        sum += i
    sum /= len(n)
    return sum


def procesar_notas(estudiantes: dict):
    dic = {}
    prom = 0
    i = 0
    for item in range(len(sorted(estudiantes))):
        temp = {}
        med = media((list(estudiantes.values()))[item])
        temp ["promedio"] = med
        if med > prom:
            prom = med
            i = item
        if med >= 11:
            temp ["estado"] = "Aprobado"
        else:
            temp["estado"] = "Desaprobado"
        dic[sorted(estudiantes)[item]] = temp
    return [dic,prom,i]

print(procesar_notas(dic)[0])
print(f"{sorted(dic)[procesar_notas(dic)[2]]} obtuvo la mayor nota: {procesar_notas(dic)[1]} ")




