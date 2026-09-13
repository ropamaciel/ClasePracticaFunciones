

productos = []

def agregar_producto():
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
    print()
def eliminar_producto():
    print()
def buscar_producto_por_precio():
    print()
def salir():
    print()