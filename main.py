from config.connection import Connection


class Aescolar:
    def __init__(self, nombre):
        self.nombre = nombre

    @classmethod
    def all_aescolar(cls, data=[]):
        try:
            conn = Connection('colegio')
            records = list(conn.get_all('aescolar', {}, {
                '_id': 0,
                'nombre': 1,
            }))

            for record in records:
                print(f'Año Escolar: {record["nombre"]}')
                print('=====================')
            return records
        except Exception as e:
            print(e)

    def insert_aescolar(self):
        try:
            conn = Connection('colegio')
            conn.insert('aescolar', {
                'nombre': self.nombre,
            })
            print(
                f'Se registro el año escolar: {self.nombre}')
        except Exception as e:
            print(e)

    def update_aescolar(self):
        try:
            conn = Connection('aescolar')
            conn.update({
                'id': 8,
                'modelo': 'Motorola'
            }, {
                'precio': self.precio,
                'modelo': 'Motorola 2021'
            })
            #print(f'Se registro el modelo: {self.modelo} con el precio {self.precio}')
        except Exception as e:
            print(e)


class Nota:
    def __init__(self, nota, alumno, curso, aescolar):
        self.nota = nota
        self.alumno = alumno
        self.curso = curso
        self.aescolar = aescolar

    @classmethod
    def all_nota(cls, data=[]):
        try:
            conn = Connection('colegio')
            records = list(conn.get_all('nota', {}, {
                '_id': 0,
                'nota': 1,
                'alumno': 1,
                'curso': 1,
                'aescolar': 1
            }))

            for record in records:
                print(f'Nota: {record["nota"]}')
                print(f'Alumno: {record["alumno"]}')
                print(f'Curso: {record["curso"]}')
                print(f'Año escolar: {record["aescolar"]}')
                print('=====================')
            return records
        except Exception as e:
            print(e)

    def insert_nota(self):
        try:
            conn = Connection('colegio')
            conn.insert('nota', {
                'nota': self.nota,
                'alumno': self.alumno,
                'curso': self.curso,
                'aescolar': self.aescolar
            })
            print(
                f'Se registro la nota de : {self.alumno}')
        except Exception as e:
            print(e)

    def update_curso(self):
        try:
            conn = Connection('curso')
            conn.update({
                'id': 8,
                'modelo': 'Motorola'
            }, {
                'precio': self.precio,
                'modelo': 'Motorola 2021'
            })
            #print(f'Se registro el modelo: {self.modelo} con el precio {self.precio}')
        except Exception as e:
            print(e)


class Curso:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor

    @classmethod
    def all_curso(cls, data=[]):
        try:
            conn = Connection('colegio')
            records = list(conn.get_all('curso', {}, {
                '_id': 0,
                'nombre': 1,
                'profesor': 1
            }))

            for record in records:
                print(f'Curso: {record["nombre"]}')
                print(f'Profesor: {record["profesor"]}')
                print('=====================')
            return records
        except Exception as e:
            print(e)

    def insert_curso(self):
        try:
            conn = Connection('colegio')
            conn.insert('curso', {
                'nombre': self.nombre,
                'profesor': self.profesor
            })
            print(
                f'Se registro el curso: {self.nombre}')
        except Exception as e:
            print(e)

    def update_curso(self):
        try:
            conn = Connection('curso')
            conn.update({
                'id': 8,
                'modelo': 'Motorola'
            }, {
                'precio': self.precio,
                'modelo': 'Motorola 2021'
            })
            #print(f'Se registro el modelo: {self.modelo} con el precio {self.precio}')
        except Exception as e:
            print(e)


class Profesor:
    def __init__(self, nombre, dni, edad, correo):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad
        self.correo = correo

    @classmethod
    def all_profesor(cls, data=[]):
        try:
            conn = Connection('colegio')
            records = list(conn.get_all('profesor', {}, {
                '_id': 0,
                'nombre': 1,
                'dni': 1,
                'edad': 1,
                'correo': 1,
            }))

            for record in records:
                print(f'Nombre: {record["nombre"]}')
                print(f'DNI: {record["dni"]}')
                print(f'Edad: {record["edad"]}')
                print(f'Correo: {record["correo"]}')
                print('=====================')
            return records
        except Exception as e:
            print(e)

    def insert_profesor(self):
        try:
            conn = Connection('colegio')
            conn.insert('profesor', {
                'nombre': self.nombre,
                'dni': self.dni,
                'edad': self.edad,
                'correo': self.correo,
            })
            print(
                f'Se registro el profesor: {self.nombre}')
        except Exception as e:
            print(e)

    def update_profesor(self):
        try:
            conn = Connection('curso')
            conn.update({
                'id': 8,
                'modelo': 'Motorola'
            }, {
                'precio': self.precio,
                'modelo': 'Motorola 2021'
            })
            #print(f'Se registro el modelo: {self.modelo} con el precio {self.precio}')
        except Exception as e:
            print(e)


class Salon:
    def __init__(self, nombre, aescolar):
        self.nombre = nombre
        self.aescolar = aescolar

    @classmethod
    def all_salon(cls, data=[]):
        try:
            conn = Connection('colegio')
            records = list(conn.get_all('salon', {}, {
                '_id': 0,
                'nombre': 1,
                'aescolar': 1
            }))

            for record in records:
                print(f'Salon: {record["nombre"]}')
                print(f'Año Escolar: {record["aescolar"]}')
                print('=====================')
            return records
        except Exception as e:
            print(e)

    def insert_salon(self):
        try:
            conn = Connection('colegio')
            conn.insert('salon', {
                'nombre': self.nombre,
                'aescolar': self.aescolar
            })
            print(
                f'Se registro el salon: {self.nombre}')
        except Exception as e:
            print(e)

    def update_salon(self):
        try:
            conn = Connection('salon')
            conn.update({
                'id': 8,
                'modelo': 'Motorola'
            }, {
                'precio': self.precio,
                'modelo': 'Motorola 2021'
            })
            #print(f'Se registro el modelo: {self.modelo} con el precio {self.precio}')
        except Exception as e:
            print(e)


class Alumno:
    def __init__(self, nombre, edad, correo, salon):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.salon = salon

    @classmethod
    def all_alumno(cls, data=[]):
        try:
            conn = Connection('colegio')
            records = list(conn.get_all('alumno', {}, {
                '_id': 0,
                'nombre': 1,
                'edad': 1,
                'correo': 1,
                'salon': 1
            }))

            for record in records:
                print(f'Nombre: {record["nombre"]}')
                print(f'Edad: {record["edad"]}')
                print(f'Correo: {record["correo"]}')
                print(f'Salon: {record["salon"]}')
                print('=====================')
            return records
        except Exception as e:
            print(e)

    def insert_alumno(self):
        try:
            conn = Connection('colegio')
            conn.insert('alumno', {
                'nombre': self.nombre,
                'edad': self.edad,
                'correo': self.correo,
                'salon': self.salon,
                # 'precio': self.precio
            })
            print(
                f'Se registro el alumno: {self.nombre}')
            # print(
            #     f'Se registro el modelo: {self.modelo} con el precio {self.precio}')
        except Exception as e:
            print(e)

    def update_alumno(self):
        try:
            conn = Connection('curso')
            conn.update({
                'id': 8,
                'modelo': 'Motorola'
            }, {
                'precio': self.precio,
                'modelo': 'Motorola 2021'
            })
            #print(f'Se registro el modelo: {self.modelo} con el precio {self.precio}')
        except Exception as e:
            print(e)

    def __init__(self, salon_id, curso_id):
        self.salon_id = salon_id
        self.curso_id = curso_id
        # self.insert_curso()
        # self.create_table()

    def create_table(self):
        try:
            conn = Connection("self")
            query = '''
                CREATE TABLE IF NOT EXISTS curso_salon(
                    id SERIAL PRIMARY KEY NOT NULL,
                    salon_id INTEGER FOREIGN KEY NOT NULL
                    curso_id INTEGER FOREIGN KEY NOT NULL
                );
            '''
            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)

    @classmethod
    def all_curso_salon(cls, data=[]):
        try:
            conn = Connection('curso_salon')
            # records = conn.select(data)

            # for record in records:
            #     print(f'ID: {record[0]}')
            #     print(f'Curso: {record[1]}')
            #     print(f'Salon: {record[2]}')
            #     ID, Salon, CursoNombre
            query = '''
                SELECT s.nombre, c.nombre FROM curso_salon cs
                JOIN curso c ON cs.curso_id = c.id
                JOIN salon s ON cs.salon_id = s.id
                WHERE s.nombre = '1A'
            '''
            # query = 'SELECT * FROM curso_salon'
            records = conn.execute_my_query(query)
            print(records)
        except Exception as e:
            print(e)

    def insert_curso_salon(self):
        try:
            conn = Connection('curso_salon')
            conn.insert({
                'salon_id': self.salon_id,
                'curso_id': self.curso_id,
                # 'precio': self.precio
            })
            print(
                'Se registro el curso_salon')
            # print(
            #     f'Se registro el modelo: {self.modelo} con el precio {self.precio}')
        except Exception as e:
            print(e)

    def update_curso_salon(self):
        try:
            conn = Connection('curso')
            conn.update({
                'id': 8,
                'modelo': 'Motorola'
            }, {
                'precio': self.precio,
                'modelo': 'Motorola 2021'
            })
            #print(f'Se registro el modelo: {self.modelo} con el precio {self.precio}')
        except Exception as e:
            print(e)


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


# print(Curso_Salon.all_curso_salon())
Cole().interfaz_inicial()
