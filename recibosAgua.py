import math
############ Calcular el total a pagar para el servicio de Agua
# Leer variables e inicializacion de variables
consumo = int(input("Ingresa el consumo en m3: "))
interesMora = float(input("Ingresa el interés y mora en Soles: "))
# IGV Perú 2019
IGV18 = 0.18
# Tarifas domestico 1
cargoFijo = 4.01
tarifaAgua0a10 = 0.8362
tarifaAlcantarilla0a10 = 0.7343

tarifaAgua11a28 = 1.4369
tarifaAlcantarilla11a28 = 1.2648

tarifaAgua29amas = 3.6927
tarifaAlcantarilla29amas = 3.2495

rango1 = 11
rango2 = 29
############ Calcular el total a pagar
# Asignacion de valores a variables de tarifa
if consumo < rango1:
  servicioAgua      = round(consumo * tarifaAgua0a10, 2)
  servicioDesague   = round(consumo * tarifaAlcantarilla0a10, 2)
else:
  if consumo < rango2:
    consumo2          = consumo - 10
    servicioAgua      = round(10 * tarifaAgua0a10 + consumo2 * tarifaAgua11a28, 2)
    servicioDesague   = round(10 * tarifaAlcantarilla0a10 + consumo2 * tarifaAlcantarilla11a28, 2)
  else:
    consumo3          = consumo - 28
    servicioAgua      = round(10 * tarifaAgua0a10 + 18 * tarifaAgua11a28 + consumo3 * tarifaAgua29amas, 2)
    servicioDesague   = round(10 * tarifaAlcantarilla0a10 + 18 * tarifaAlcantarilla11a28 + consumo3 * tarifaAlcantarilla29amas, 2)
    print(10 * tarifaAlcantarilla0a10 + 18 * tarifaAlcantarilla11a28)
    print("diego ", 10 * tarifaAgua0a10 + 18 * tarifaAgua11a28)

subTotal          = round(servicioAgua + servicioDesague + cargoFijo + interesMora, 2)
igv               = round((servicioAgua + servicioDesague + cargoFijo) * IGV18, 2)
totalSinRedondear = subTotal + igv
redondeo          = round(round((totalSinRedondear) * 10 - math.floor((totalSinRedondear) * 10), 2) * 0.1, 2)
totalPagar        = round(totalSinRedondear - redondeo, 2)

############ Mostrar Resultados
print(f"TOTAL A PAGAR:             {totalPagar}")
