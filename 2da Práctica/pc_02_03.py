"""Se requiere verificar una lista de números de diferentes países, el
área de soporte al cliente recibe diariamente ciento de números en
distintos formatos. Estos números pueden venir con o sin código,
espacios, guines, paréntesis, o hasta textos no válido

- Crear la función de normalizar_telefonos(numeros, pais_defecto) la
cual para sus parámetros tendrá las siguientes especificaciones:
numeros: lista con números telefónicos
pais_defecto: en caso no tenga un número un prefijo lo agrega de
acuerdo al país ( “PE”->”+51”, “AR”->”+54”, “CL”->”+56”)
Si el prefijo no existe entre los ya mencionados indicar un mensaje
que no es válido y que debe ingresar un prefijo válido
- Devolverá un dict con:
“válidos”: una lista de números con formato: +<código><numeroNacional>
“invalidos”: lista con los números o valores inválidos y al inicio de esa
lista agregar el valor de “NO VÁLIDOS”
- No mutará la lista de entrada original"""


numeros = ["958152325", "519515482", "abz", "Fiorella"]
def normalizar_telefonos(numeros: list, pais_defecto = "PE"):
    dic = {}
    válidos = []
    no_válidos = ["NO VÁLIDOS"]
    n_c = numeros.copy()
    num = "0"
    if pais_defecto == "PE":
        num = "+51 "
    elif pais_defecto == "AR":
        num = "+54 "
    elif pais_defecto == "CL":
        num = "+56 "
    else:
        print("país no válido")
        return (-1)
    for i in n_c:
        if i[0:4] == num:
            i.replace(i[0:4], "    ")
            i.lstrip()
            if i.isdigit():
                i = num + i
                válidos.append(i)
            else:
                no_válidos.append(i)
        else:
            if i.isdigit():
                i = num + i
                válidos.append(i)
            else:
                no_válidos.append(i)
    dic["válidos"] = válidos
    dic["inválidos"] = no_válidos
    return dic


print(normalizar_telefonos(numeros))