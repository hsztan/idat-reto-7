from config.connection import Connection


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
