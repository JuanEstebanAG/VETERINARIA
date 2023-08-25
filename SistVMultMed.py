class Medicamento:
    def __init__(self):
        self.__nombre = ''
        self.__dosis = 0

    def verNombre(self):
        return self.__nombre

    def verDosis(self):
        return self.__dosis

    def asignarNombre(self, med):
        self.__nombre = med

    def asignarDosis(self, med):
        self.__dosis = med


class Mascota:
    def __init__(self):
        self.__nombre = ''
        self.__historia = 0
        self.__tipo = ''
        self.__peso = ''
        self.__fecha_ingreso = ''
        self.__lista_medicamentos = []

    def verNombre(self):
        return self.__nombre

    def verHistoria(self):
        return self.__historia

    def verTipo(self):
        return self.__tipo

    def verPeso(self):
        return self.__peso

    def verFecha(self):
        return self.__fecha_ingreso

    def verLista_Medicamentos(self):
        return self.__lista_medicamentos

    def asignarNombre(self, n):
        self.__nombre = n

    def asignarHistoria(self, nh):
        self.__historia = nh

    def asignarTipo(self, t):
        self.__tipo = t

    def asignarPeso(self, p):
        self.__peso = p

    def asignarFecha(self, f):
        if self.validarFecha(f):
            self.__fecha_ingreso = f
        else:
            print('Error: La fecha debe tener el formato dd/mm/aaaa')

    def asignarLista_Medicamentos(self, n):
        self.__lista_medicamentos = n

    def validarFecha(self, fecha):
        try:
            dia, mes, anio = fecha.split('/')
            dia = int(dia)
            mes = int(mes)
            anio = int(anio)
            if dia < 1 or dia > 31 or mes < 1 or mes > 12 or anio < 1900 or anio > 2100:
                return False
            return True
        except:
            return False


class sistemaV:
    def __init__(self):
        self.__diccionario_mascotas = {}
        self.__lista_medicamentos = []

    def verificarExiste(self, historia):
        return historia in self.__diccionario_mascotas

    def verificarMedicamento(self, nombre):
        for m in self.__lista_medicamentos:
            if nombre == m.verNombre():
                return True
        return False

    def verNumeroMascotas(self):
        return len(self.__diccionario_mascotas)

    def ingresarMascota(self, mascota):
        if self.verificarExiste(mascota.verHistoria()):
            print('Error: Ya existe una mascota con el número de historia clínica ingresado')
        else:
            self.__diccionario_mascotas[mascota.verHistoria()] = mascota

    def verFechaIngreso(self, historia):
        mascota = self.__diccionario_mascotas.get(historia)
        if mascota:
            return mascota.verFecha()
        return None

    def verMedicamento(self, historia):
        mascota = self.__diccionario_mascotas.get(historia)
        if mascota:
            return mascota.verLista_Medicamentos()
        return None

    def eliminarMascota(self, historia):
        if historia in self.__diccionario_mascotas:
            del self.__diccionario_mascotas[historia]
            return True
        return False

    def agregarMedicamento(self, medicamento):
        if self.verificarMedicamento(medicamento.verNombre()):
            print('Error: Ya existe un medicamento con el mismo nombre')
        else:
            self.__lista_medicamentos.append(medicamento)

    def eliminarMedicamento(self, historia, nombre_medicamento):
        mascota = self.__diccionario_mascotas.get(historia)
        if mascota:
            medicamentos = mascota.verLista_Medicamentos()
            for medicamento in medicamentos:
                if medicamento.verNombre() == nombre_medicamento:
                    medicamentos.remove(medicamento)
                    return True
        return False


def main():
    servicio_hospitalario = sistemaV()
    while True:
        menu = int(input('''Elija la opción que desea realizar: 
                       1. Ingresar una mascota.
                       2. Ver fecha de ingreso.
                       3. Ver número de mascotas en el servicio.
                       4. Ver medicamentos que se están administrando.
                       5. Eliminar mascota.
                       6. Agregar medicamento.
                       7. Eliminar medicamento de una mascota.
                       8. Salir. 
                       -> '''))
        if menu == 1:
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print('No hay espacio...')
                continue
            historia = int(input('Digite la historia clínica de la mascota: '))
            if servicio_hospitalario.verificarExiste(historia) == False:
                nombre = input('Ingrese el nombre de la mascota: ')
                tipo = input('Ingrese el tipo de mascota (felino o canino): ')
                peso = int(input('Ingrese el peso de la mascota: '))
                fecha = input('Ingrese la fecha de ingreso (dd/mm/aaaa): ')
                nm = int(input('Ingrese cantidad de medicamentos: '))
                lista_med = []

                for i in range(0, nm):
                    nombre_medicamento = input('Ingrese el nombre del medicamento: ')
                    dosis = int(input('Ingrese la dosis: '))
                    medicamento = Medicamento()
                    medicamento.asignarNombre(nombre_medicamento)
                    medicamento.asignarDosis(dosis)
                    lista_med.append(medicamento)

                mas = Mascota()
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarPeso(peso)
                mas.asignarTipo(tipo)
                mas.asignarFecha(fecha)
                mas.asignarLista_Medicamentos(lista_med)
                servicio_hospitalario.ingresarMascota(mas)

            else:
                print('Ya existe la mascota con el número de historia clínica')

        elif menu == 2:
            q = int(input('Ingrese la historia clínica de la mascota: '))
            fecha = servicio_hospitalario.verFechaIngreso(q)
            if fecha != None:
                print('La fecha de ingreso de la mascota es: ' + fecha)
            else:
                print('La historia clínica ingresada no corresponde con ninguna mascota en el sistema.')

        elif menu == 3:
            numero = servicio_hospitalario.verNumeroMascotas()
            print('El número de pacientes en el sistema es: ' + str(numero))

        elif menu == 4:
            q = int(input('Ingrese la historia clínica de la mascota: '))
            medicamento = servicio_hospitalario.verMedicamento(q)
            if medicamento != None:
                print('Los medicamentos suministrados son: ')
                for m in medicamento:
                    print(f'\n- {m.verNombre()}')
            else:
                print('La historia clínica ingresada no corresponde con ninguna mascota en el sistema.')

        elif menu == 5:
            q = int(input('Ingrese la historia clínica de la mascota: '))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q)
            if resultado_operacion == True:
                print('Mascota eliminada del sistema con éxito')
            else:
                print('No se ha podido eliminar la mascota')

        elif menu == 6:
            nombre_medicamento = input('Ingrese el nombre del medicamento: ')
            dosis = int(input('Ingrese la dosis: '))
            medicamento = Medicamento()
            medicamento.asignarNombre(nombre_medicamento)
            medicamento.asignarDosis(dosis)
            servicio_hospitalario.agregarMedicamento(medicamento)

        elif menu == 7:
            q = int(input('Ingrese la historia clínica de la mascota: '))
            nombre_medicamento = input('Ingrese el nombre del medicamento a eliminar: ')
            resultado_operacion = servicio_hospitalario.eliminarMedicamento(q, nombre_medicamento)
            if resultado_operacion == True:
                print('Medicamento eliminado de la mascota con éxito')
            else:
                print('No se ha podido eliminar el medicamento')

        elif menu == 8:
            print('Usted ha salido del sistema de servicio de hospitalización...')
            break

        else:
            print('Usted ingresó una opción no válida, intentelo nuevamente...')


if __name__ == '__main__':
    main()


