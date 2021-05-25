from config.connection import Connection


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
