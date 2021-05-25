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
