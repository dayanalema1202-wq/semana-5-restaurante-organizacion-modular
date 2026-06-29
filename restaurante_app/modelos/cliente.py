# modelos/cliente.py
# Modulo del modelo Cliente.
# Representa a una persona que visita el restaurante.
# Ademas de sus datos personales, registra si tiene alguna
# restriccion alimentaria y cuantas veces ha visitado el local.


class Cliente:
    """Representa a un cliente del restaurante."""

    def __init__(self, id_cliente, nombre, telefono, restriccion):
        self.id_cliente = id_cliente    # identificador del cliente
        self.nombre = nombre            # nombre completo
        self.telefono = telefono        # numero de contacto
        self.restriccion = restriccion  # ninguna, vegetariano, vegano, celiaco
        self.visitas = 0                # contador de visitas al restaurante
        self.puntos = 0                 # puntos acumulados por fidelidad

    def registrar_visita(self):
        """Suma una visita y otorga 10 puntos de fidelidad."""
        self.visitas += 1
        self.puntos += 10

    def canjear_puntos(self, cantidad):
        """Descuenta puntos si el cliente tiene suficientes."""
        if self.puntos >= cantidad:
            self.puntos -= cantidad
            print(self.nombre + " canjeo " + str(cantidad) + " puntos.")
        else:
            print(self.nombre + " no tiene suficientes puntos.")

    def actualizar_telefono(self, nuevo_telefono):
        """Actualiza el numero de telefono del cliente."""
        self.telefono = nuevo_telefono

    def __str__(self):
        return (f"ID {self.id_cliente} | {self.nombre} | Tel: {self.telefono} "
                f"| Restriccion: {self.restriccion} "
                f"| Visitas: {self.visitas} | Puntos: {self.puntos}")
