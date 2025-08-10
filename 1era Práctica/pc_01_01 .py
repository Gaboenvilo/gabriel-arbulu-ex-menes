#1. Usando los tipos de datos y sus conversiones realizar lo siguiente. (4 ptos)

#Reglas:
#- Asignar en variables los datos de tu nombre, salario, edad y compañia para un
#usuario e identificar sus tipos de variables
#- Edad tiene que ser tipo string, para usarla más adelante tiene que aplicarse una
#conversión de datos
#- Identificar si la edad es mayor a 30, mostrar un mensaje ingresado "Usted
#tiene un bono de 10% en el mes de diciembre" caso contrario mostrar "Usted
#tiene un bono del 5% en el mes diciembre"
#- Mostrar el bono final que es: potencia de 2 del salario más el 5 o 10 % de su
#salario, según corresponda.


tu_nombre= "Alfredo" #string
salario= 3500.50 #float
edad= "40" #string
compañía= "Seguros Rimac" #string


if int(edad) > 30:
    print("Usted tiene un bono de 10% en el mes de diciembre:",salario**2+salario*10/100)
elif int(edad) < 30:
    print("Usted tiene un bono del 5% en el mes diciembre",salario**2+salario*5/100)

