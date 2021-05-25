from config.connection import Connection


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
