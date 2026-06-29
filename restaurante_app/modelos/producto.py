# modelos/producto.py
# Modulo del modelo Producto.
# Representa un plato del menu del restaurante. Ademas del
# nombre y precio, registra si contiene alergenos comunes
# y el tipo de coccion para informar al cliente.


class Producto:
    """Representa un plato o bebida disponible en el restaurante."""

    def __init__(self, codigo, nombre, tipo_coccion, precio, tiene_alergenos):
        self.codigo = codigo                    # codigo unico del plato
        self.nombre = nombre                    # nombre del plato
        self.tipo_coccion = tipo_coccion        # Frito, Asado, Al vapor, Crudo
        self.precio = precio                    # precio en dolares
        self.tiene_alergenos = tiene_alergenos  # True si contiene alergenos
        self.oferta = False                     # True si esta en oferta

    def poner_en_oferta(self, precio_oferta):
        """Activa la oferta y cambia el precio al precio de oferta."""
        self.oferta = True
        self.precio = precio_oferta

    def quitar_oferta(self, precio_normal):
        """Desactiva la oferta y restaura el precio normal."""
        self.oferta = False
        self.precio = precio_normal

    def __str__(self):
        alergeno = "contiene alergenos" if self.tiene_alergenos else "sin alergenos"
        en_oferta = " [EN OFERTA]" if self.oferta else ""
        return (f"{self.codigo} | {self.nombre} | {self.tipo_coccion} "
                f"| ${self.precio:.2f}{en_oferta} | {alergeno}")
