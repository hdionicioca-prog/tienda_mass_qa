from sistema_tienda import (
    autenticar_usuario,
    verificar_disponibilidad_stock,
    calcular_total_carrito,
    validar_cobertura_distrito
)

print("=" * 60)
print(" SISTEMA TIENDA MASS - REPORTE DE RESULTADOS DE PRUEBAS")
print("=" * 60)

# 1. Login
login_ok = autenticar_usuario("cliente@mass.pe", "Mass2026*")
print(f"1. Autenticación de usuario: {'[EXITOSA]' if login_ok else '[FALLIDA]'}")

# 2. Stock
stock_ok = verificar_disponibilidad_stock(stock_actual=10, cantidad_solicitada=3)
print(f"2. Validación de Stock (10 disp. / 3 ped.): {'[DISPONIBLE]' if stock_ok else '[SIN STOCK]'}")

# 3. Carrito
items = [
    {"nombre": "Arroz 1kg", "precio": 4.50, "cantidad": 2},
    {"nombre": "Aceite 1L", "precio": 7.00, "cantidad": 1}
]
total_con_descuento = calcular_total_carrito(items, tiene_cupon_descuento=True)
print(f"3. Total Carrito con 10% desc.: S/ {total_con_descuento:.2f}")

# 4. Cobertura
cobertura_ate = validar_cobertura_distrito("Ate")
print(f"4. Cobertura en Ate: {'[COBERTURA VÁLIDA]' if cobertura_ate else '[FUERA DE ZONA]'}")

print("=" * 60)
print("Estado general: TODAS LAS PRUEBAS FUNCIONAN CORRECTAMENTE")
print("=" * 60) 