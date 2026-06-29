# servicios/restaurante.py
# Modulo del servicio Restaurante.
# Coordina las operaciones principales del sistema: administra
# el menu y los clientes, filtra platos segun restricciones
# alimentarias y genera reportes de fidelidad.

from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """Administra los productos y clientes del restaurante."""

    def __init__(self, nombre, tipo_cocina):
        self.nombre = nombre            # nombre del restaurante
        self.tipo_cocina = tipo_cocina  # tipo de cocina que ofrece
        self.productos = []             # lista de objetos Producto
        self.clientes = []              # lista de objetos Cliente

    # gestion de productos

    def agregar_producto(self, producto):
        """Agrega un producto al menu del restaurante."""
        self.productos.append(producto)

    def mostrar_menu(self):
        """Imprime todos los productos del menu."""
        print("\nMenu de " + self.nombre + " (" + self.tipo_cocina + ")")
        print("-" * 62)
        if not self.productos:
            print("No hay productos registrados.")
        for p in self.productos:
            print("  " + str(p))
        print("-" * 62)

    def menu_sin_alergenos(self):
        """Muestra solo los platos que no contienen alergenos."""
        print("\nPlatos sin alergenos:")
        encontrados = [p for p in self.productos if not p.tiene_alergenos]
        if not encontrados:
            print("  No hay platos sin alergenos en el menu.")
        for p in encontrados:
            print("  " + str(p))

    def buscar_producto(self, codigo):
        """Devuelve el producto con ese codigo o None si no existe."""
        for p in self.productos:
            if p.codigo == codigo:
                return p
        return None

    # gestion de clientes

    def registrar_cliente(self, cliente):
        """Registra un cliente en el sistema."""
        self.clientes.append(cliente)

    def mostrar_clientes(self):
        """Imprime la lista de clientes registrados."""
        print("\nClientes registrados en " + self.nombre)
        print("-" * 62)
        if not self.clientes:
            print("No hay clientes registrados.")
        for c in self.clientes:
            print("  " + str(c))
        print("-" * 62)

    def clientes_por_restriccion(self, restriccion):
        """Lista los clientes que tienen una restriccion alimentaria."""
        print("\nClientes con restriccion '" + restriccion + "':")
        encontrados = [c for c in self.clientes if c.restriccion == restriccion]
        if not encontrados:
            print("  No hay clientes con esa restriccion.")
        for c in encontrados:
            print("  " + str(c))

    def cliente_mas_fiel(self):
        """Muestra el cliente con mas visitas registradas."""
        if not self.clientes:
            print("No hay clientes registrados.")
            return
        fiel = max(self.clientes, key=lambda c: c.visitas)
        print("\nCliente mas fiel: " + fiel.nombre +
              " con " + str(fiel.visitas) + " visita(s).")

    def resumen(self):
        """Muestra un resumen general del restaurante."""
        en_oferta = sum(1 for p in self.productos if p.oferta)
        print("\nResumen de " + self.nombre)
        print("  Tipo de cocina     : " + self.tipo_cocina)
        print("  Productos en menu  : " + str(len(self.productos)) +
              " (" + str(en_oferta) + " en oferta)")
        print("  Clientes registrados: " + str(len(self.clientes)))

    def __str__(self):
        return "Restaurante " + self.nombre + " | " + self.tipo_cocina
