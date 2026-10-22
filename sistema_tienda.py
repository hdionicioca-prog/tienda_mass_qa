"""
Módulo de lógica de negocio para la evaluación de Tienda Mass.
Incluye 4 funciones clave del flujo operativo.
"""

def autenticar_usuario(correo: str, password: str) -> bool:
    """Valida formato y credenciales básicas de acceso."""
    if not correo or "@" not in correo:
        return False
    # Simulación de usuario registrado
    if correo == "cliente@mass.pe" and password == "Mass2026*":
        return True
    return False


def verificar_disponibilidad_stock(stock_actual: int, cantidad_solicitada: int) -> bool:
    """Verifica si la cantidad pedida es válida y existe stock suficiente."""
    if cantidad_solicitada <= 0:
        return False
    return stock_actual >= cantidad_solicitada


def calcular_total_carrito(items: list, tiene_cupon_descuento: bool = False) -> float:
    """
    Calcula el subtotal sumando precio * cantidad.
    Aplica 10% de descuento si tiene cupón promocional.
    """
    if not items:
        return 0.0

    subtotal = sum(item["precio"] * item["cantidad"] for item in items)
    
    if tiene_cupon_descuento:
        subtotal *= 0.90  # Aplica 10% de descuento

    return round(subtotal, 2)


def validar_cobertura_distrito(distrito: str) -> bool:
    """Valida si el distrito ingresado está dentro del alcance de reparto (Ate)."""
    coberturas_activas = ["ATE", "ATE VITARTE"]
    return distrito.strip().upper() in coberturas_activas