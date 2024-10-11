# main.py
from mi_clase import Alumno1
from ClaseAlumno import Alumno

# Crear una instancia de la clase Alumno
alumno1 = Alumno1("Juan", 20)

# Usar los métodos de la clase
print(alumno1.obtener_nombre())  # Salida: Juan
print(alumno1.obtener_edad())    # Salida: 20

# Cambiar los valores
alumno1.cambiar_nombre("Carlos")
alumno1.cambiar_edad(21)

print(alumno1.obtener_nombre())  # Salida: Carlos
print(alumno1.obtener_edad())    # Salida: 21


# Esto es del archivo ClaseAlumno
registro_alumno = {}

# Bucle para ingresar datos de 3 alumnos
for i in range(3):
    alumno = Alumno()  # Crear instancia de Alumno
    nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
    apellido_paterno = input(f"Ingrese el apellido paterno del alumno {i + 1}: ")
    apellido_materno = input(f"Ingrese el apellido materno del alumno {i + 1}: ")
    no_control = int(input(f"Ingrese el número de control del alumno {i + 1}: "))
    semestre = int(input(f"Ingrese el semestre del alumno {i + 1}: "))

    # Asignar valores al alumno
    alumno.set_nombre(nombre)
    alumno.set_apellido_paterno(apellido_paterno)
    alumno.set_apellido_materno(apellido_materno)
    alumno.set_no_control(no_control)
    alumno.set_semestre(semestre)

    # Guardar el alumno en el diccionario
    registro_alumno[i] = alumno

# Mostrar los nombres completos de los alumnos registrados
for i in range(3):
    print(f"Nombre completo del alumno {i + 1}: {registro_alumno[i].get_nombre_completo()}")

