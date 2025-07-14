
trabajo_final_python.py

Autor: Landaburo, Walter Nahuel (desarrollador autodidacta).
Fecha de creación: 2025 - 07 - 14.

Descripción:
-----------
Este script implementa una simulación de un registro de productos.
Cada producto tiene un ID único que lo identifica.

Permite:
 1) agregar datos: nombre, descripcion, cantidad, precio y categoria a la tabla 'productos'.
 2) mostrar todos los productos de la tabla 'productos'.
 3) Actualizar datos en un producto de elección del usuario. No puede modificar el ID asignado automáticamente; se requiere el ID para localizar el producto.
 4) Eliminar un producto a elección del usuario. Se requiere el ID para localizar el producto.
 4) Buscar un producto a elección del usuario. Realiza la búsqueda comparando 'ID', 'nombre' o 'categoria'.
 6) Filtrar la tabla 'productos', muestra mlos que tengan una cantidad igual o inferior a la que define el usuario.
 7) Salir del programa ingresando el número "7".
 
El programa está diseñado para interactuar con el usuario/a.

Estructura general:
------------------
• base de datos para guardar información.
• SQLite3 para interactuar con la base de datos.
• docstring para documentar las acciones al recorrer el script.

Notas:
------
• módulo Colorama. ROJO para errores, CIAN para información, VERDE para confirmar una operación exitosa.
• el dato "nombre" puede contener números. Dando libertad al usuario para identificarse


Licencia:
--------
Este código es de uso educativo y puede ser modificado con fines personales o de aprendizaje.

Compatibilidad:
---------------
Python 3.0


Gratitud:
---------
• Talento Tech: una oportunidad que me ha permitido redirigir mi energía y seguir creciendo con esperanza. Necesitaba actualizar mi software y ustedes me han abierto la puerta 🚪.
• Tomás Torchinsky Landau y Agustín Alamino. Sin ellos no habría curso, no hubiera tenido la oportunidad de ver after class ni relacionarme por Discord.
• colegas: una genialidad el grupo de Discord, las devoluciones de desconocidos, algo maravilloso para sumar, aportar y continuar progresando.
• Alzate, Carlos: un compañero a destacar, qme brindo devoluciones y facilito mi acceso y continuidad en este camino con su conocimiento, experiencia, su ayuda. Me genero consciencia de algo que no tuve jajaja y con sus mensajes estimulo mi desarrollo; le estoy muy agradecido por su guía.
