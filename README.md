# Sistema de Gestion de Restaurante

Estudiante: Dayana Valeria Lema Saldaña  
Asignatura: Programacion Orientada a Objetos  
Semana: 5

---

## Descripcion del sistema

El proyecto es un sistema basico de gestion para el restaurante "La Terraza
de Dayana", desarrollado en Python aplicando Programacion Orientada a Objetos.

El sistema permite registrar platos del menu con su tipo de coccion e
indicacion de alergenos, gestionar ofertas en productos, registrar clientes
con sus restricciones alimentarias, acumular puntos de fidelidad por visita,
canjear puntos, filtrar el menu sin alergenos, listar clientes por restriccion
e identificar al cliente mas fiel del restaurante.

El objetivo de la tarea es demostrar la organizacion modular del proyecto,
la separacion de responsabilidades entre archivos y el uso correcto de las
importaciones y los conceptos basicos de la POO.

---

## Estructura del proyecto

```
restaurante_app/
    modelos/
        __init__.py
        producto.py      - clase Producto
        cliente.py       - clase Cliente
    servicios/
        __init__.py
        restaurante.py   - clase Restaurante
    main.py              - punto de arranque del programa
```

### Descripcion de cada archivo

- modelos/producto.py: define la clase Producto, que representa un plato o
  bebida del menu. Sus atributos son codigo, nombre, tipo de coccion, precio,
  indicador de alergenos y estado de oferta. Los metodos permiten activar o
  desactivar una oferta cambiando el precio del producto.

- modelos/cliente.py: define la clase Cliente, que representa a una persona
  registrada en el restaurante. Guarda el id, nombre, telefono, restriccion
  alimentaria, contador de visitas y puntos acumulados. Sus metodos permiten
  registrar visitas, canjear puntos y actualizar el telefono.

- servicios/restaurante.py: define la clase Restaurante, que es el servicio
  central del sistema. Administra el menu y los clientes, filtra platos sin
  alergenos, agrupa clientes por restriccion alimentaria e identifica al
  cliente mas fiel segun el numero de visitas.

- main.py: es el punto de arranque. Crea todos los objetos, los registra en
  el servicio y ejecuta los metodos del sistema para mostrar su funcionamiento.

---

## Conceptos de POO aplicados

- Clases: Producto, Cliente y Restaurante.
- Constructor __init__: inicializa los atributos de cada objeto al crearlo.
- Atributos: definidos segun el contexto del restaurante (tipo de coccion,
  alergenos, restriccion alimentaria, puntos de fidelidad, estado de oferta).
- Metodos: gestionan y muestran la informacion de los objetos de cada clase.
- Metodo especial __str__: implementado en las tres clases para representar
  cada objeto como texto legible al imprimirlo en consola.
- Importaciones entre archivos: main.py importa desde modelos y servicios;
  restaurante.py importa los modelos que necesita.

---

## Como ejecutar el programa

Desde la carpeta raiz del repositorio:

```
python restaurante_app/main.py
```

El programa imprime el menu completo, los platos sin alergenos, los clientes
registrados, el filtro por restriccion alimentaria, el cliente mas fiel, una
busqueda de producto por codigo y el resumen general del restaurante.

---

## Reflexion sobre modularizar el software

Separar el proyecto en modulos con una responsabilidad bien definida permite
que cada parte del sistema se pueda leer, modificar y probar de forma
independiente. En este caso los modelos representan las entidades del problema
sin preocuparse por la logica del negocio, el servicio concentra las
operaciones que conectan esas entidades, y main.py solo coordina la ejecucion.

Esa separacion tiene ventajas concretas: si se cambia como se calculan los
puntos de fidelidad, solo se modifica cliente.py sin afectar nada mas. Si se
agrega un nuevo tipo de filtro al menu, se agrega un metodo en restaurante.py.
Eso hace que el codigo sea mas ordenado, facil de mantener y preparado para
crecer, que son razones fundamentales por las que la Programacion Orientada a
Objetos es tan usada en el desarrollo de software profesional.
