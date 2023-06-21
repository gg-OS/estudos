from random import randint, choice


class Node:

    def __init__(self, car, plate, prev=None):
        self.plate = plate
        self.car = car
        self.prev = prev


class Parking:

    def __init__(self):
        self.top = None

    def park(self, car, plate):
        new_car = Node(car, plate)
        if self.top is None:
            self.top = new_car
        else:
            mem = self.top
            self.top = new_car
            self.top.prev = mem
        return

    def withdrawl(self, plate):
        itr = self.top
        done = True
        if self.get_plate(plate) == 0:
            print('Esse carro não se encontra no estacionamento.')
            return
        else:
            while itr and done:
                if self.top.plate == plate:
                    done = False
                    self.top = self.top.prev
                elif itr.prev.plate == plate:
                    done = False
                    itr.prev = itr.prev.prev
                itr = itr.prev
        return

    def show_previous_cars(self, plate):
        itr = self.top
        parking_lot = ''
        if self.get_plate(plate) == 0:
            print('Esse carro não se encontra nos estacionamento.')
            return
        else:
            while itr.plate != plate:
                parking_lot = ' <- ' + str(itr.car) + parking_lot
                itr = itr.prev
            parking_lot = '[' + parking_lot[4:] + ']'
        return parking_lot

    def show_line(self):
        itr = self.top
        parking_lot = ''
        for j in range(0, self.size()):
            parking_lot = ' <- ' + str(itr.car) + parking_lot
            itr = itr.prev
        parking_lot = '[None' + parking_lot
        parking_lot += ']'
        return parking_lot

    def size(self):
        s = 0
        itr = self.top
        if itr is None:
            print('A pilha está vazia.')
        else:
            while itr:
                s += 1
                itr = itr.prev
        return s

    def get_plate(self, plate):
        itr = self.top
        p = 0
        while itr:
            if itr.plate == plate:
                p += 1
            itr = itr.prev
        return p

    def get_top(self):
        return str(self.top.prev.plate)


def plate_gen():
    letras = 'ABCDEFGHIJKLMNOPQRSTUWVXYZ'
    placa = ''
    for j in range(7):
        if j == 3 or j == 5 or j == 6:
            placa += str(randint(0, 9))
        else:
            placa += str(choice(letras))
    return placa


nomes = ['Ford Ka',
         'Chevrolet Onix',
         'Kia Soul',
         'BMW i350',
         'Hyundai ix35',
         'Toyota Corolla']

carros = {}

for i in range(len(nomes)):
    try:
        carros.update({plate_gen(): nomes[i]})
    except KeyError:
        carros.update({plate_gen(): nomes[i]})

parking = Parking()

print(carros)
print()

for cliente in carros.keys():
    parking.park(carros[cliente], cliente)

print(parking.show_line())
print(parking.get_top())
remover = input('Insira a placa do carro que quer remover: ')

print(f'\nPara remover o carro {carros[remover]}, será necessário mover os carros '
      f'{parking.show_previous_cars(remover)}')
parking.withdrawl(remover)

print(f'\nAssim ficou o estacionamento após a remoção: {parking.show_line()}')
