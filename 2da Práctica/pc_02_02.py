"""- Crear una función normalizar_nombres(nombres)
- El parámetro recibe una lista de string de nombres (6 como mínimo)
- Este quitará el espacio antes y después si lo hubiera
- Convierte en tipo título
- Si hubiera más nombre los debe separar (si debe haber el caso)
- Devuelve también eliminando duplicados manteniendo el orden de la primera
- No mutará la lista original"""

nombres = ["   Gabriel    alvarez", "Gabriel", "Rocio MEdina", "Paolo Barraza", "Hernán Cortés", "Ana Carolina"]
def normalizar_nombres(lista: list):
    nueva = []
    dic = {}
    if len(lista) < 6:
        print ("lista inválida")
        return 0
    for i in lista:
        temp = i.split()
        for j in temp:
            j = j.title().rstrip().lstrip()
            nueva.append(j)
    backup_lista = nueva.copy()
    nueva.reverse()
    for i in range(len(backup_lista)):
        if nueva.count(nueva[i]) > 1:
            dic[nueva[i]] = len(backup_lista) - i - 1
    nueva.reverse()
    for i in sorted(dic):
        while (nueva.count(i) != 0):
            nueva.remove(i)

        nueva.insert(dic[i], i)
    return(nueva)


print(f"lista actualizada: {normalizar_nombres(nombres)}")