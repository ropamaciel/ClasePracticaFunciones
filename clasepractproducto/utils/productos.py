

productos = []

def agregar_producto():
    print("\n===== AGREGAR PRODUCTO =====")
    try:
        nombre = input("Ingrese el nombre del producto: ").strip()
        
        if not nombre:
            print("El nombre del producto no puede estar vacío.")
            return
        
        precio = float(input("Ingrese el precio del producto: "))
        # Validar que el precio sea un número positivo
        cantidad = float(input("Ingrese la cantidad del producto: "))

        if precio < 0:
            print("El precio del producto no puede ser negativo.")
            return
        
        if cantidad < 0:
            print("La cantidad del producto no puede ser negativa.")
            return

        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }
        productos.append(producto)

        print(f"Producto: {producto['nombre']} agregado correctamente.")


    except ValueError:
        print("Error: El precio debe ser un número válido.")
    finally:
        print("Producto agregado correctamente.")






def mostrar_producto():
    print("\n============LISTA DE PRODUCTOS============")

    if not productos:
        print("No hay productos registrados.")
        return
    
    for indice, producto in enumerate(productos, start=1):
        print(f"""Nombre: {producto['nombre']}
           Precio: ${producto['precio']:.2f}
           Cantidad: {producto['cantidad']}
            =====================================   
    """)



def eliminar_producto():
    print("\n===== ELIMINAR PRODUCTO =====")

    if not productos:
        print("No hay productos registrados.")
        return

    nombre_buscado = input("Ingrese el nombre del producto: ").strip()

    for producto in productos:
        if producto["nombre"].lower() == nombre_buscado.lower():
            productos.remove(producto)

            print(
                f"Producto '{producto['nombre']}' "
                "eliminado correctamente."
            )
            return

    print("Producto no encontrado.")
 

def buscar_producto():
    print("\n===== BUSCAR PRODUCTO =====")

    if not productos:
        print("No hay productos registrados.")
        return

    nombre_buscado = input("Ingrese el nombre del producto: ").strip()

    for producto in productos:
        if producto["nombre"].lower() == nombre_buscado.lower():
            print("\nProducto encontrado:")
            print(f"Nombre: {producto['nombre']}")
            print(f"Precio: ${producto['precio']:.2f}")
            print(f"Cantidad: {producto['cantidad']}")
            return

    print("Producto no encontrado.")


def buscar_por_precio(productos, precio_maximo):
    
    encontrados = []

    for producto in productos:
        if producto["precio"] <= precio_maximo:
            encontrados.append(producto)

    return encontrados 


def mostrar_estadisticas():
    print("\n===== ESTADÍSTICAS =====")

    if not productos:
        print("No hay productos registrados.")
        return

    cantidad_productos = len(productos)

    valor_total = 0

    for producto in productos:
        valor_total += (
            producto["precio"] *
            producto["cantidad"]
        )

    print(f"Cantidad de productos: {cantidad_productos}")
    print(f"Valor total del inventario: ${valor_total:.2f}")  


def salir():
    print()