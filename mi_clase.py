# mi_clase.py
class Alumno1:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad      # Atributo privado

    def obtener_nombre(self):
        return self.__nombre

    def obtener_edad(self):
        return self.__edad

    def cambiar_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def cambiar_edad(self, nueva_edad):
        self.__edad = nueva_edad
