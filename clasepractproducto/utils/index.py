from productos import (
   agregar_producto,
   mostrar_producto,
   buscar_por_precio,
   buscar_producto,
   eliminar_producto,
   mostrar_estadisticas
)
from menu import mostrar_menu



def index():
   while True:
      mostrar_menu()

      op = input("Seleccionar:").strip()

      match op:
         case "1":
            agregar_producto()
         case "2":
            mostrar_producto()
         case "3":
            buscar_por_precio()
         case "4":
            eliminar_producto()
         case "5":
            mostrar_estadisticas()
         case "7":
            
       
if __name__ == "__main__":
   index()



    
