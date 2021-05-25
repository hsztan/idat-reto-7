from config.connection import Connection


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
