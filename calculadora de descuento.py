def calcular_descuento(monto_total, porcentaje_descuento=10):
  """
  Calcula el descuento aplicado a un monto total de compra.

  Parámetros:
    monto_total: El monto total de la compra (float).
    porcentaje_descuento: El porcentaje de descuento a aplicar (float).

  Retorno:
    El monto del descuento calculado (float).
  """

  descuento = monto_total * (porcentaje_descuento / 100)
  return descuento

# Ejemplo de uso

monto_compra_1 = 100
descuento_1 = calcular_descuento(monto_compra_1)

print(f"Monto total: {monto_compra_1:.2f}")
print(f"Descuento aplicado ({porcentaje_descuento}%): {descuento_1:.2f}")

monto_compra_1 = 200
porcentaje_descuento_2 = 20
descuento_2 = calcular_descuento(monto_compra_1, porcentaje_descuento_2)

print(f"\nMonto total: {monto_compra_2:.2f}")
print(f"Descuento aplicado ({porcentaje_descuento_2}%): {descuento_3:.2f}")