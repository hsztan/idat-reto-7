from models.Aescolar import Aescolar
from models.Alumno import Alumno
from models.Curso import Curso
from models.Nota import Nota
from models.Profesor import Profesor
from models.Salon import Salon


class Cole:
    def __init__(self):
        pass

    def interfaz_inicial(self):
        try:
            while True:
                print('''
                    BIENVENIDO AL SISTEMA DE GESTION ESCOLAR
                    Seleccione el número de su opción:
                    1) Gestionar Alumnos
                    2) Gestionar Profesores
                    3) Gestionar Salones
                    4) Gestionar Cursos
                    5) Gestionar Notas
                    6) Salir del Progama
                ''')
                opcion = input('>')
                if (opcion == '1'):
                    self.interfaz_alumno()
                if (opcion == '2'):
                    self.interfaz_profesor()
                if (opcion == '3'):
                    self.interfaz_salon()
                if (opcion == '4'):
                    self.interfaz_curso()
                if (opcion == '5'):
                    self.interfaz_nota()
                if (opcion == '6'):
                    exit()
                else:
                    print('Ingrese una opción válida')
        except Exception as e:
            print(e)

    def interfaz_nota(self):
        while True:
            print('''
                NOTAS
                1) Ver Notas
                2) Crear Nota
                3) Regresar
            ''')
            opcion = input('>')
            if (opcion == '1'):
                Nota.all_nota()
            if (opcion == '2'):
                self.ingresar_nota()
            if (opcion == '3'):
                return
            else:
                print('Ingrese una opción válida')

    def interfaz_curso(self):
        while True:
            print('''
                CURSOS
                1) Mostrar Cursos
                2) Crear Curso
                3) Regresar
            ''')
            opcion = input('>')
            if (opcion == '1'):
                Curso.all_curso()
            if (opcion == '2'):
                self.ingresar_curso()
            if (opcion == '3'):
                return
            else:
                print('Ingrese una opción válida')

    def interfaz_salon(self):
        while True:
            print('''
                SALONES
                1) Mostrar Salones
                2) Crear Salon
                3) Regresar
            ''')
            opcion = input('>')
            if (opcion == '1'):
                Salon.all_salon()
            if (opcion == '2'):
                self.ingresar_salon()
            if (opcion == '3'):
                return
            else:
                print('Ingrese una opción válida')

    def interfaz_profesor(self):
        while True:
            print('''
                PROFESORES
                1) Mostrar Profesores
                2) Crear Profesor
                3) Regresar
            ''')
            opcion = input('>')
            if (opcion == '1'):
                Profesor.all_profesor()
            if (opcion == '2'):
                self.ingresar_profesor()
            if (opcion == '3'):
                return
            else:
                print('Ingrese una opción válida')

    def interfaz_alumno(self):
        while True:
            print('''
                ALUMNOS
                1) Mostrar Alumnos
                2) Crear Alumno
                3) Regresar
            ''')
            opcion = input('>')
            if (opcion == '1'):
                Alumno.all_alumno()
            if (opcion == '2'):
                self.ingresar_alumno()
            if (opcion == '3'):
                return
            else:
                print('Ingrese una opción válida')

    def ingresar_nota(self):
        Alumno.all_alumno()
        alumno_id = input('Escoger ID del alumno > ')
        Curso.all_curso()
        curso_id = input('Escoger ID del curso > ')
        Aescolar.all_aescolar()
        aescolar_id = input('Escoger ID del año escolar > ')
        nota = input('Ingrese la nota del curso > ')
        Nota(nota, alumno_id, curso_id, aescolar_id).insert_nota()

    def ingresar_curso(self):
        nombre = input('Ingresar nombre del curso > ')
        Profesor.all_profesor()
        profesor_id = input('Ingresar ID de profesor > ')
        Curso(nombre, profesor_id).insert_curso()

    def ingresar_salon(self):
        nombre = input('Ingresar nombre del salón > ')
        Aescolar.all_aescolar()
        aescolar_id = input('Ingresar año escolar > ')
        Salon(nombre, aescolar_id).insert_salon()

    def ingresar_profesor(self):
        nombre = input('Nombre del profesor > ')
        dni = input('DNI > ')
        edad = input('Edad > ')
        correo = input('Correo > ')
        Profesor(nombre, dni, edad, correo).insert_profesor()

    def ingresar_alumno(self):
        nombre = input('Nombre del alumno > ')
        edad = input('Edad del alumno > ')
        correo = input('Correo del alumno > ')
        Salon.all_salon()
        print('Seleccione el salón: > ')
        salon_id = input('>')
        Alumno(nombre, edad, correo, salon_id).insert_alumno()
