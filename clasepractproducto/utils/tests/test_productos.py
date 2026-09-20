import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
import productos

#decoradores con el fixture se ejecuta

@pytest.fixture(autouse=True)
def limpiar_productos():
    productos.productos.clear()  # limpio la lista de productos antes de cada prueba
    yield #limpio la lista de productos después de cada prueba
    productos.productos.clear()  # limpio la lista de productos después de cada prueba


@pytest.fixture
def datos_base():    
    productos.productos.extend([
        {"nombre": "Teclado", "precio": 2000, "cantidad": 5},
        {"nombre": "Monitor", "precio": 8000, "cantidad": 2},
        {"nombre": "Parlante", "precio": 5000, "cantidad": 15}   
    ])
    return productos.productos  
   

def test_agregar_producto_exitoso(monkeypatch):
    
    entrada = iter(["Mouse", "1500","3"])
    monkeypatch.setattr("builtins.input", lambda _: next(entrada))

    productos.agregar_producto()

    assert len(productos.productos) == 1

def test_buscar_productos_existentes(datos_base):
    resultado = productos.buscar_por_precio(datos_base, precio_maximo=6000)

    assert len(resultado) == 2
   # assert any(p["nombre"] == "Teclado" for p in resultado)
    #assert any(p["nombre"] == "Parlante" for p in resultado)


def test_agregar_producto_precio_negativo(monkeypatch):
    entrada = iter(["Mouse", "-1500", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(entrada))

    productos.agregar_producto()

    assert len(productos.productos) == 0  # No se debe agregar el producto con precio negativo


def test_eliminar_producto(monkeypatch, datos_base):
    
    monkeypatch.setattr("builtins.input", lambda _: "Teclado")  # Simula la entrada del nombre del producto a eliminar)
    productos.eliminar_producto()

    assert len(productos.productos) == 2  # Verifica que la lista de productos esté vacía después de eliminar el producto
    assert productos.productos[0]["nombre"] == "Monitor"  # Verifica que el producto eliminado sea el correcto  

