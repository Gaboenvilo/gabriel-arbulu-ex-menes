# - Caso: Calculadora de propinas
# Crea un programa que permita ingresar el total de una cuenta en un restaurante,
# el porcentaje de propina que desea dejar el cliente y el número de personas que
# dividirán la cuenta. El programa debe mostrar:
# El monto total con propina.
# El monto que debe pagar cada persona (con 2 decimales).
# Un mensaje será personalizado, indicará si el monto individual supera los 100
# soles, mostrando un mensaje de advertencia si es el caso.
# Entrada esperada (por input):
# Total de la cuenta: float
# Porcentaje de propina: float
# Número de personas: int
# Salida ejemplo (output):
# Monto total con propina: S/. 230.00
# Cada persona debe pagar: S/. 115.00
# ¡Advertencia! El monto por persona supera los S/. 100

total_de_la_cuenta = 260.5
porcentaje_de_propina = 10 / 100
número_de_personas = 3

monto_total_con_propina = total_de_la_cuenta + total_de_la_cuenta * porcentaje_de_propina
pago_por_persona = monto_total_con_propina / número_de_personas

print("Monto total con propina: {}".format(monto_total_con_propina))
print("Cada persona debe pagar: {:.2F}".format(pago_por_persona))

if pago_por_persona > 100:
    print("¡Advertencia! El monto por persona supera los S/. 100")
elif pago_por_persona < 100:
    print("¡Estás bien! El monto por persona no supera los S/. 100")
