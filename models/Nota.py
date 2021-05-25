from config.connection import Connection


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
