import pytest
from sistema_tienda import (
    autenticar_usuario,
    verificar_disponibilidad_stock,
    calcular_total_carrito,
    validar_cobertura_distrito
)

def test_autenticar_usuario():
    print("\n--- [Prueba 1: Autenticación] ---")
    res1 = autenticar_usuario("cliente@mass.pe", "Mass2026*")
    print(f"Intento login correcto -> Resultado: {res1} (Esperado: True)")
    assert res1 is True

    res2 = autenticar_usuario("cliente@mass.pe", "clave_invalida")
    print(f"Intento login clave incorrecta -> Resultado: {res2} (Esperado: False)")
    assert res2 is False


def test_verificar_disponibilidad_stock():
    print("\n--- [Prueba 2: Verificación de Stock] ---")
    res1 = verificar_disponibilidad_stock(stock_actual=10, cantidad_solicitada=5)
    print(f"Stock 10, pide 5 -> Resultado: {res1} (Esperado: True)")
    assert res1 is True

    res2 = verificar_disponibilidad_stock(stock_actual=2, cantidad_solicitada=5)
    print(f"Stock 2, pide 5 -> Resultado: {res2} (Esperado: False)")
    assert res2 is False


def test_calcular_total_carrito():
    print("\n--- [Prueba 3: Cálculo del Carrito y Descuento] ---")
    productos = [
        {"nombre": "Arroz 1kg", "precio": 4.50, "cantidad": 2},
        {"nombre": "Aceite 1L", "precio": 7.00, "cantidad": 1}
    ]
    total_normal = calcular_total_carrito(productos, tiene_cupon_descuento=False)
    print(f"Total sin descuento -> S/ {total_normal:.2f} (Esperado: 16.00)")
    assert total_normal == 16.00

    total_descuento = calcular_total_carrito(productos, tiene_cupon_descuento=True)
    print(f"Total con 10% de descuento -> S/ {total_descuento:.2f} (Esperado: 14.40)")
    assert total_descuento == 14.40


def test_validar_cobertura_distrito():
    print("\n--- [Prueba 4: Cobertura Geográfica] ---")
    res1 = validar_cobertura_distrito("Ate")
    print(f"Distrito 'Ate' -> Cobertura: {res1} (Esperado: True)")
    assert res1 is True

    res2 = validar_cobertura_distrito("Miraflores")
    print(f"Distrito 'Miraflores' -> Cobertura: {res2} (Esperado: False)")
    assert res2 is False