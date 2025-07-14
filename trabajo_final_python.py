import sqlite3
from colorama import Fore, Style, init
init(autoreset=True)

def crear_tabla():
    
    """
    SQL Base de datos 
    Crear tabla si no existe 
    """
    #Establecer la conexión a la base de datos
    conexion = sqlite3.connect("inventario.db")
    
    #Crear un objeto cursor
    cursor = conexion.cursor()
    
    #Crear una tabla si no existe 
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT UNIQUE NOT NULL,
            descripcion TEXT NOT NULL,
            cantidad INTEGER CHECK (cantidad >= 1) NOT NULL,
            precio REAL CHECK (precio >= 1) NOT NULL,
            categoria TEXT NOT NULL
            )
    ''')    
    
    print("✅ Tabla 'productos' creada exitosamente.")


    #Confirmar cambios y cerrar la conexión 
    conexion.commit()
    conexion.close()


def agregar_producto(nombre, descripcion, cantidad, precio, categoria):
    
    """
    Inserta un nuevo producto en la tabla 'productos' 
    """
    
    
    #SQL Base de datos 
    #Establecer la conexión a la base de datos
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    
    try:
        #Iniciar transacción 
        conexion.execute('BEGIN TRANSACTION')
        
        #Insertar datos en la tabla
        cursor.execute('''
            INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
            VALUES (?, ?, ?, ?, ?)
            ''', (nombre, descripcion, cantidad, precio, categoria))
    
        #Confirmar cambios
        conexion.commit()
        print(Fore.GREEN + "✅ Producto agregado exitosamente.")
        
    except sqlite3.IntegrityError:
        print(Fore.RED + "⚠️ El nombre ingresado ya está registrado.")
        
    except sqlite3.Error as e:
        #Si ocurre un error, revertir cambios
        conexion.rollback()
        print(Fore.RED + f"Error al registrar el producto '{e}'")
        
    finally:
        #Cerrar conexión 
        conexion.close()
    
    
        

def mostrar_productos():
    
    """
    Muestra todos los productos de la tabla 'productos' 
    """
    
    #SQL Base de datos 
    #Establecer la conexión a la base de datos
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    
    #Recuperar todos los registros de la tabla 'productos' 
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()
    
    if not productos:
        print(Fore.YELLOW + "⚠️ La tabla se encuentra vacía.")
    
    else:

        print(Fore.GREEN + "\n=== Lista de productos ===")
        for p in productos:
            print(f"ID: {p[0]}, Nombre: {p[1]}, Descripción: {p[2]}, Cantidad: {p[3]}, Precio: ${p[4]:.2f}, Categoría: {p[5]}")
        
    #Cerrar conexión 
    conexion.close()
    
def actualizar_producto():
     
     """
     Modifica un valor de un producto existente en la tabla'productos'. 
     No modifica el ID.
     """
     
    #SQL Base de datos 
    #Establecer la conexión a la base de datos
     conexion = sqlite3.connect("inventario.db")
     cursor = conexion.cursor()

     
         
    

    #Solicitar al usuario el ID del producto que desea modificar 
     id_producto = input("Ingrese el ID del producto que desea modificar: ").strip()
     
     if not id_producto.isdigit():
         print(Fore.RED + "❌ El ID tiene que ser un número.")

     else:
             
     #Solicitar al usuario especifique lo que desea modificar del producto 
         print("¿Qué desea modificar del producto?.")
         print("Ingrese 'N' para nombre. \nIngrese 'D' para descripción. \nIngrese 'CAN' para cantidad. \nIngrese 'P' para precio. \nIngrese 'CAT' para categoría.")
         opcion = input("/nIngrese su elección: ").strip().lower()
    
         if opcion.isdigit():
             print(Fore.RED + "❌ Dato no válido.")
        
    
        #Actualizar nombre 
         if opcion == "n":
             nuevo = input("Nuevo nombre: ").strip().lower()
             cursor.execute('UPDATE productos SET nombre = ? WHERE id = ?',
             (nuevo, id_producto))
        
            #Confirmar cambio
             conexion.commit()
        
          
             print(Fore.GREEN + f"✅ Producto con ID: {id_producto} actualizado correctamente.")
        
             cursor.execute('SELECT * FROM productos WHERE id = ?', (id_producto))
             producto_actualizado = cursor.fetchone()
        
            #Verificar cambio 
             print("\n=== PRODUCTO ACTUALIZADO ===")
             print(f"ID: {producto_actualizado[0]}, Nombre: {producto_actualizado[1]}, Descripción: {producto_actualizado[2]}, Cantidad: {producto_actualizado[3]}, Precio: ${producto_actualizado[4]:.2f}, Categoría: {producto_actualizado[5]}")
        
            #Cerrar conexión 
             conexion.close()
    
        #Actualizar descripcion
         if opcion == "d":
             nuevo = input("Nueva descripción: ").strip().lower()
             cursor.execute('UPDATE productos SET descripcion = ? WHERE id = ?',
             (nuevo, id_producto))
        
            #Confirmar cambio
             conexion.commit()
            
             print(Fore.GREEN + f"✅ Producto con ID: {id_producto} actualizado correctamente.")
        
             cursor.execute('SELECT * FROM productos WHERE id = ?', (id_producto))
             producto_actualizado = cursor.fetchone()
        
            #Verificar cambio 
             print("\n=== PRODUCTO ACTUALIZADO ===")
             print(f"ID: {producto_actualizado[0]}, Nombre: {producto_actualizado[1]}, Descripción: {producto_actualizado[2]}, Cantidad: {producto_actualizado[3]}, Precio: ${producto_actualizado[4]:.2f}, Categoría: {producto_actualizado[5]}")
        
            #Cerrar conexión 
             conexion.close()
    
        #Actualizar cantidad 
         if opcion == "can":
             nuevo = input("Nueva cantidad: ").strip()
             
             if not nuevo.isdigit():
                 print(Fore.RED + "❌ La cantidad tiene que ser un número entero.")
             
             else:
                 cursor.execute('UPDATE productos SET cantidad = ? WHERE id = ?',
                 (nuevo, id_producto))
        
                #Confirmar cambio
                 conexion.commit()
            
                 print(Fore.GREEN + f"✅ Producto con ID: {id_producto} actualizado correctamente.")
        
                 cursor.execute('SELECT * FROM productos WHERE id = ?', (id_producto))
                 producto_actualizado = cursor.fetchone()
        
                #Verificar cambio 
                 print("\n=== PRODUCTO ACTUALIZADO ===")
                 print(f"ID: {producto_actualizado[0]}, Nombre: {producto_actualizado[1]}, Descripción: {producto_actualizado[2]}, Cantidad: {producto_actualizado[3]}, Precio: ${producto_actualizado[4]:.2f}, Categoría: {producto_actualizado[5]}")
        
                #Cerrar conexión 
                 conexion.close()
    
        #Actualizar precio     
         if opcion == "p":
             nuevo = input("Nuevo precio: ").strip()
             
             if not nuevo.isdigit():
                 print(Fore.RED + "❌ El precio debe ser un número.")
             
             else:
                 cursor.execute('UPDATE productos SET precio = ? WHERE id = ?',
                 (nuevo, id_producto))
        
                #Confirmar cambio
                 conexion.commit()
        
                 print(Fore.GREEN + f"✅ Producto con ID: {id_producto} actualizado correctamente.")
        
                 cursor.execute('SELECT * FROM productos WHERE id = ?', (id_producto))
                 producto_actualizado = cursor.fetchone()
        
                #Verificar cambio 
                 print("\n=== PRODUCTO ACTUALIZADO ===")
                 print(f"ID: {producto_actualizado[0]}, Nombre: {producto_actualizado[1]}, Descripción: {producto_actualizado[2]}, Cantidad: {producto_actualizado[3]}, Precio: ${producto_actualizado[4]:.2f}, Categoría: {producto_actualizado[5]}")
        
                #Cerrar conexión 
                 conexion.close()
    
            #Actualizar categoria    
         if opcion == "cat":
             nuevo = input("Nueva categoría: ").strip().lower()
             cursor.execute('UPDATE productos SET categoria = ? WHERE id = ?',
             (nuevo, id_producto))
        
             #Confirmar cambio
             conexion.commit()
        
             print(Fore.GREEN + f"✅ Producto con ID: {id_producto} actualizado correctamente.")
        
             cursor.execute('SELECT * FROM productos WHERE id = ?', (id_producto))
             producto_actualizado = cursor.fetchone()
        
            #Verificar cambio 
             print("\n=== PRODUCTO ACTUALIZADO ===")
             print(f"ID: {producto_actualizado[0]}, Nombre: {producto_actualizado[1]}, Descripción: {producto_actualizado[2]}, Cantidad: {producto_actualizado[3]}, Precio: ${producto_actualizado[4]:.2f}, Categoría: {producto_actualizado[5]}")
        
            #Cerrar conexión 
             conexion.close()
    
def eliminar_producto():
    
    """
    Elimina un producto existente en la tabla 'productos'.
    """
    
    #SQL Base de datos 
    #Establecer la conexión a la base de datos
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    
    #Solicitar al usuario el ID del producto que desea eliminar 
    id_producto = input("Ingrese el ID del producto que desea eliminar: ").strip()
    
    if not id_producto.isdigit():
        print(Fore.RED + "❌ Ingrese un número de ID válido.")
        
    else:
        
        try:
            #Iniciar transacción 
            conexion.execute('BEGIN TRANSACTION')
            
            #Eliminar producto 
            cursor.execute('DELETE FROM productos WHERE id=?',
            (id_producto,))
        
            #Confirmar cambio 
            conexion.commit()
            print(Fore.GREEN + f"✅ El producto con ID: {id_producto} fue eliminado correctamente.")
        
        except sqlite3.Error as e:
            #Si ocurre un error, revertir cambios
            conexion.rollback()
            print(Fore.RED + f"Error al eliminar el producto '{e}'")
            
        finally:
            #Cerrar conexión 
            conexion.close()
    
def buscar_producto():
    
    """
    Muestra un producto existente en la tabla 'productos'.
    """
    
    #SQL Base de datos 
    #Establecer la conexión a la base de datos
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    
    #Solicitar al usuario el ID, nombre o categoria para realizar la búsqueda del producto
    print("Puede realizar la búsqueda ingresando el ID, nombre o categoría del producto.")
    print("\nSi desea buscar un producto por su ID, ingrese 'ID'.\nSi desea buscar un producto por su nombre, Ingrese 'N'.\nSi desea buscar un producto por su de categoría, ingrese 'C'.")
    
    buscar = input("Ingrese la opción de su preferencia: ").strip().lower()
    
    
    if buscar.isdigit():
        print(Fore.RED + "❌ Dato no válido.")
    
    
    #Buscar por ID    
    elif buscar == "id":
        id_buscar = input("Ingrese el ID buscado: ").strip()
        
        if not id_buscar.isdigit():
            print(Fore.RED + "❌ Tiene que ser un número válido.")
        
        else:
            cursor.execute('SELECT id, nombre, descripcion, cantidad, precio, categoria FROM productos WHERE id = ?', (id_buscar,))
            productos = cursor.fetchall()
        
            if not productos:
                print(Fore.YELLOW + "⚠️ No se encontro un producto que coincida con el dato ingresado.")
        
            print(Fore.GREEN + f"=== \nProductos que coincidan con {id_buscar} ===")
            for p in productos:
                print(f"ID: {p[0]}, Nombre: {p[1]}, Descripción: {p[2]}, Cantidad: {p[3]}, Precio: ${p[4]:.2f}, Categoría: {p[5]}")
        
            
            #Cerrar conexión 
            conexion.close()     
    
    
    #Buscar por nombre    
    elif buscar == "n":

        nombre_buscar = input("Ingrese el nombre del producto: ").strip().lower()
        
        cursor.execute('SELECT id, nombre, descripcion, cantidad, precio, categoria FROM productos WHERE nombre = ?', (nombre_buscar,))
        productos = cursor.fetchall()
        
        if not productos:
            print(Fore.YELLOW + "⚠️ No se encontro un producto que coincida con el dato ingresado.")
        
        print(Fore.GREEN + f"=== \nProductos que coincidan con {nombre_buscar} ===")
        for p in productos:
            print(f"ID: {p[0]}, Nombre: {p[1]}, Descripción: {p[2]}, Cantidad: {p[3]}, Precio: ${p[4]:.2f}, Categoría: {p[5]}")
        
       #Cerrar conexión 
        conexion.close()      
            
    
    #Buscar por categoria   
    elif buscar == "c":

        categoria_buscar = input("Ingrese la categoría: ").strip().lower()
        
        if categoria_buscar.isdigit():
            print(Fore.RED + "❌ Dato no válido.")
        
        else:

            cursor.execute('SELECT id, nombre, descripcion, cantidad, precio, categoria FROM productos WHERE categoria = ?', (categoria_buscar,))
            productos = cursor.fetchall()
        
            if not productos:
                print(Fore.YELLOW + "⚠️ No se encontro un producto que coincida con el dato ingresado.")
        
            print(Fore.GREEN + f"=== \nProductos que coincidan con {categoria_buscar} ===")
            for p in productos:
                print(f"ID: {p[0]}, Nombre: {p[1]}, Descripción: {p[2]}, Cantidad: {p[3]}, Precio: ${p[4]:.2f}, Categoría: {p[5]}")
        
             
            #Cerrar conexión 
            conexion.close()    
        
    else:
        print(Fore.RED + "❌ Dato no válido.")

def filtrar_producto_cantidad():
    
    """
    Muestra todos los productos existentes en la tabla 'productos' con una cantidad igual o inferior a la definida por el usuario.
    """
    
    #SQL Base de datos 
    #Establecer la conexión a la base de datos
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    
    print("Mostrar productos con una cantidad de unidades igual o inferior a lo ingresado por el usuario.")
    
    #Solicitar al usuario el ID del producto que desea modificar 
    limite = input("Ingrese la cantidad de unidades para filtrar la tabla de productos: ").strip()
    
    if not limite.isdigit():
        print(Fore.RED + "❌ Dato no válido.")
    
    else:
        #Recuperar los registros de la tabla 'productos' con cantidad menor o igual a limite
        cursor.execute('SELECT * FROM productos WHERE cantidad <= ?',
        (limite,))
        productos = cursor.fetchall()
    
        print(Fore.GREEN + f"\n=== Lista de productos con una cantidad menor o igual a {limite} ===")
        for p in productos:
            print(f"ID: {p[0]}, Nombre: {p[1]}, Descripción: {p[2]}, Cantidad: {p[3]}, Precio: ${p[4]:.2f}, Categoría: {p[5]}")
        
        #Cerrar conexión 
        conexion.close()    
    
    
def menu():
    
    """
    Menú de opciones.
    El usuario decide la acción a realizar.
    """
    
    while True:
        print(Fore.BLUE + "\n=== Menú de gestión de productos ===")
        print(Fore.WHITE + "1. AGREGAR PRODUCTO")
        print(Fore.WHITE + "2. MOSTRAR PRODUCTOS")
        print(Fore.WHITE + "3. ACTUALIZAR PRODUCTO")
        print(Fore.WHITE + "4. ELIMINAR PRODUCTO")
        print(Fore.WHITE + "5. BUSCAR PRODUCTO")
        print(Fore.WHITE + "6. FILTRAR PRODUCTOS POR CANTIDAD")
        print(Fore.WHITE + "7. SALIR DEL PROGRAMA")
        
        
        opcion = input("Ingrese el número de la acción a realizar: ").strip()
        
            
        if opcion == "1":
            
            print(Fore.CYAN + "\n=== Agregar producto===")
            #Solicitar datos al usuario 
            nombre = input("Ingrese el nombre del producto: ").strip()
            descripcion = input("Ingrese la descripción del producto: ").strip().lower()
            cantidad = input("Ingrese la cantidad disponible: ").strip()
            precio = input("Ingrese el precio del producto: ").strip()
            categoria = input("Ingrese la categoría del producto: ").strip().lower()
            
            
            #Validar 'nombre', 'descripcion' y 'categoria' no estén vacíos 
            if not nombre or not descripcion or not categoria:
                print(Fore.RED + "❌ Los campos no pueden estar vacíos.")
                
            
            #Validar 'cantidad' y 'precio' sean números
            if not cantidad.isdigit() or not precio.isdigit():
                print(Fore.RED + "❌ La 'cantidad' y el 'precio' deben ser números enteros.")
                

            else:
                agregar_producto(nombre, descripcion, cantidad, precio, categoria)     
                
    
        elif opcion == "2":
            
            mostrar_productos()
            
            
        elif opcion == "3":
            #SQL Base de datos 
            #Establecer la conexión a la base de datos
            conexion = sqlite3.connect("inventario.db")
            cursor = conexion.cursor()
                            
            #Recuperar todos los registros de la tabla 'productos' 
            cursor.execute('SELECT * FROM productos')
            productos = cursor.fetchall()
            if not productos:
                print(Fore.YELLOW + "⚠️ No hay productos registrados en la base de datos.")
        

            else:
                actualizar_producto()
            
            conexion.close()
            
        elif opcion == "4":
            #SQL Base de datos 
            #Establecer la conexión a la base de datos
            conexion = sqlite3.connect("inventario.db")
            cursor = conexion.cursor()
                            
            #Recuperar todos los registros de la tabla 'productos' 
            cursor.execute('SELECT * FROM productos')
            productos = cursor.fetchall()
            
            if not productos:
                print(Fore.YELLOW + "⚠️ No hay productos registrados en la base de datos.")
          
            else:
                eliminar_producto()

            conexion.close()    
            
        elif opcion == "5":
            #SQL Base de datos 
            #Establecer la conexión a la base de datos
            conexion = sqlite3.connect("inventario.db")
            cursor = conexion.cursor()
                            
            #Recuperar todos los registros de la tabla 'productos' 
            cursor.execute('SELECT * FROM productos')
            productos = cursor.fetchall()

            if not productos:
                print(Fore.YELLOW + "⚠️ No hay productos registrados en la base de datos.")
            
            else:
                buscar_producto()

            conexion.close()    
            
        elif opcion == "6":
            #SQL Base de datos 
            #Establecer la conexión a la base de datos
            conexion = sqlite3.connect("inventario.db")
            cursor = conexion.cursor()
                            
            #Recuperar todos los registros de la tabla 'productos' 
            cursor.execute('SELECT * FROM productos')
            productos = cursor.fetchall()

            if not productos:
                print(Fore.YELLOW + "⚠️ No hay productos registrados en la base de datos.")
            
            else:
                filtrar_producto_cantidad()

            conexion.close()    
            
        elif opcion == "7":
            print("Gracias por usar la aplicación. Saliendo ....")
            break 
            
        else:
            print("❌ Opción inválida. Por favor, intente nuevamente.")
            continue 

crear_tabla()

menu()
            