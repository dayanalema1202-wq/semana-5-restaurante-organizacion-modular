# main.py
# Punto de arranque del programa.
# Se crean los objetos, se registran en el servicio principal
# y se ejecutan los metodos para demostrar el funcionamiento
# del sistema de gestion del restaurante.

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def main():

    # crear el servicio principal
    restaurante = Restaurante("La Terraza de Dayana", "Cocina fusión andina")
    print(restaurante)

    # crear objetos Producto
    p1 = Producto("M01", "Locro de papa",           "Al vapor", 4.00, False)
    p2 = Producto("M02", "Llapingachos con chorizo","Asado",    5.50, True)
    p3 = Producto("M03", "Ensalada de quinua",      "Crudo",    4.50, False)
    p4 = Producto("M04", "Trucha a la plancha",     "Asado",    7.00, False)
    p5 = Producto("M05", "Chicha morada",           "Crudo",    1.75, False)
    p6 = Producto("M06", "Fritada con mote",        "Frito",    6.00, True)

    # agregar productos al menu
    for producto in [p1, p2, p3, p4, p5, p6]:
        restaurante.agregar_producto(producto)

    # poner en oferta un plato
    p1.poner_en_oferta(3.00)

    # mostrar el menu completo
    restaurante.mostrar_menu()

    # mostrar solo platos sin alergenos
    restaurante.menu_sin_alergenos()

    # crear objetos Cliente
    c1 = Cliente(1, "Dayana Valeria Lema Saldana", "0987001100", "ninguna")
    c2 = Cliente(2, "Pablo Toro",                  "0991002200", "vegetariano")
    c3 = Cliente(3, "Ana Lucía Vega",              "0976003300", "celiaco")
    c4 = Cliente(4, "Juan Morocho",                "0983004400", "ninguna")

    # registrar visitas de los clientes
    for _ in range(4):
        c1.registrar_visita()
    for _ in range(2):
        c2.registrar_visita()
    c3.registrar_visita()
    for _ in range(6):
        c4.registrar_visita()

    # canjear puntos de un cliente
    c4.canjear_puntos(30)

    # actualizar telefono de un cliente
    c3.actualizar_telefono("0970009999")

    # registrar los clientes en el sistema
    restaurante.registrar_cliente(c1)
    restaurante.registrar_cliente(c2)
    restaurante.registrar_cliente(c3)
    restaurante.registrar_cliente(c4)

    # mostrar todos los clientes
    restaurante.mostrar_clientes()

    # filtrar clientes por restriccion alimentaria
    restaurante.clientes_por_restriccion("vegetariano")

    # mostrar el cliente mas fiel
    restaurante.cliente_mas_fiel()

    # buscar un producto por codigo
    print("\nBusqueda del producto M04:")
    encontrado = restaurante.buscar_producto("M04")
    if encontrado:
        print("  " + str(encontrado))

    # resumen general
    restaurante.resumen()


if __name__ == "__main__":
    main()
