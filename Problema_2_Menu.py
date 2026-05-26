"""
Fase 5 - Evaluación Final POA
Estudiante: Emanuel Vargas
Problema 2: Gestión de precios de un menú de restaurante con promociones.
"""

def calcular_precio_final(precio_base, categoria, categoria_objetivo, umbral_precio):
    """
    Calcula el precio final de un producto.
    Aplica un 15% de descuento si cumple con la categoría objetivo y supera el umbral.
    """
    descuento = 0.15  # 15% de descuento
    
    # Verificamos si cumple ambas condiciones de la promoción
    if categoria == categoria_objetivo and precio_base > umbral_precio:
        valor_descuento = precio_base * descuento
        precio_final = precio_base - valor_descuento
    else:
        # Si no cumple, se mantiene el precio base
        precio_final = precio_base
        
    return precio_final

def main():
    # 1. Creación de la matriz del menú: [Nombre del Producto, Categoría, Precio Base]
    # Se incluyen 6 productos de diversas categorías.
    menu_restaurante = [
        ["Mojarra Frita", "Plato Principal", 35000],
        ["Arroz de Lisa", "Plato Principal", 18000],
        ["Sopa de Guandúl", "Plato Principal", 25000],
        ["Jugo de Corozo", "Bebidas", 8000],
        ["Limonada de Coco", "Bebidas", 10000],
        ["Enyucado", "Postres", 12000]
    ]

    # Parámetros de la promoción definidos por el negocio
    CATEGORIA_PROMOCION = "Plato Principal"
    UMBRAL_MINIMO = 20000

    print("=" * 60)
    print("   SISTEMA DE GESTIÓN DE PRECIOS - MENÚ DEL RESTAURANTE")
    print("=" * 60)
    print(f"-> Promoción activa: 15% de descuento en '{CATEGORIA_PROMOCION}'")
    print(f"-> Condición: Precio base mayor a ${UMBRAL_MINIMO}\n")

    # 2. Recorremos la matriz para procesar cada producto
    for producto in menu_restaurante:
        nombre = producto[0]
        categoria = producto[1]
        precio_base = producto[2]

        # Llamado al módulo/función para calcular el precio final
        precio_final = calcular_precio_final(precio_base, categoria, CATEGORIA_PROMOCION, UMBRAL_MINIMO)

        # 3. Salida de datos en consola
        if precio_final < precio_base:
            # Si hubo descuento, lo mostramos destacado
            print(f"Producto: {nombre} | Base: ${precio_base} | FINAL: ${precio_final} (¡Promo Aplicada!)")
        else:
            # Si no hubo descuento
            print(f"Producto: {nombre} | Base: ${precio_base} | FINAL: ${precio_final}")
            
    print("=" * 60)

# Punto de entrada del programa
if __name__ == "__main__":
    main()
