# hipoteca.py
# Archivo de ejemplo
# Ejercicio de hipoteca
# hipoteca.py

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mesesTotales = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    pago_mensual_total = pago_mensual
    if (mesesTotales >= pago_extra_mes_comienzo and mesesTotales <= pago_extra_mes_fin):
        pago_mensual_total = pago_mensual_total + pago_extra
    saldo = saldo * (1+tasa/12) - pago_mensual_total
    total_pagado = total_pagado + pago_mensual_total
    mesesTotales = mesesTotales + 1

print('Total pagado', round(total_pagado, 2), 'en', mesesTotales, 'meses')
