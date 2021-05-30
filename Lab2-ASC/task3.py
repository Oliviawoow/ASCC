"""
Coffee Factory: A multiple producer - multiple consumer approach

Generate a base class Coffee which knows only the coffee name
Create the Espresso, Americano and Cappuccino classes which inherit the base class knowing that
each coffee type has a predetermined size.
Each of these classes have a get message method

Create 3 additional classes as following:
    * Distributor - A shared space where the producers puts coffees and the consumers takes them
    * CoffeeFactory - An infinite loop, which always sends coffees to the distributor
    * User - Another infinite loop, which always takes coffees from the distributor

The scope of this exercise is to correctly use threads, classes and synchronization objects.
The size of the coffee (ex. small, medium, large) is chosen randomly everytime.
The coffee type is chosen randomly everytime.

Example of output:

Consumer 65 consumed espresso
Factory 7 produced a nice small espresso
Consumer 87 consumed cappuccino
Factory 9 produced an italian medium cappuccino
Consumer 90 consumed americano
Consumer 84 consumed espresso
Factory 8 produced a strong medium americano
Consumer 135 consumed cappuccino
Consumer 94 consumed americano
"""
from threading import Semaphore, Thread
from random import choice


class Coffee:
    """ Base class """
    def __init__(self, coffee_type, size):
        self.coffee_type = coffee_type
        self.size = size

    def get_name(self):
        """ Returns the coffee name """
        return self.coffee_type

    def get_size(self):
        """ Returns the coffee size """
        return self.size


class Espresso(Coffee):
    # Espresso implementation
    def __init__(self, size):
        Coffee.__init__(self, "espresso", size)

    # Output message
    def get_message(self):
        return "a nice " + self.get_size() + " " + self.get_name()


class Americano(Coffee):
    # Americano implementation
    def __init__(self, size):
        Coffee.__init__(self, "americano", size)

    # Output message
    def get_message(self):
        return "a strong " + self.get_size() + " " + self.get_name()


class Cappuccino(Coffee):
    # Cappuccino implementation
    def __init__(self, size):
        Coffee.__init__(self, "cappuccino", size)

    # Output message
    def get_message(self):
        return "an italian " + self.get_size() + " " + self.get_name()


TYPES = [Espresso, Americano, Cappuccino]
SIZES = ['small', 'medium', 'large']


# Returns a random coffee type
def my_random_coffee():
    return choice(TYPES)


# Returns a random coffee size
def my_random_size():
    return choice(SIZES)


class Distributor:
    def __init__(self, n):
        self.full = n
        self.arr = []
        self.sem_prod = Semaphore(self.full)
        self.sem_con = Semaphore(0)

    def produce(self, coffee, name, no):
        self.sem_prod.acquire()
        self.arr.append(coffee)
        print(name, no, 'produced', coffee.get_message())
        self.sem_con.release()

    def consume(self, name, no):
        self.sem_con.acquire()
        print(name, no, 'consumed', self.arr.pop().get_name())
        self.sem_prod.release()


# Producer
class CoffeeFactory:
    def __init__(self, name, no, distributor):
        self.name = name
        self.no = no
        self.distributor = distributor

    def process(self):
        # infinite loop
        while True:
            coffee_class = my_random_coffee()
            self.distributor.produce(coffee_class(my_random_size()), self.name, self.no)


# Consumer
class User:
    def __init__(self, name, no, distributor):
        self.name = name
        self.no = no
        self.distributor = distributor

    def process(self):
        # infinite loop
        while True:
            self.distributor.consume(self.name, self.no)


def main():
    nr_prod = 10
    nr_con = 25
    distributor = Distributor(nr_prod)
    threads = []

    for i in range(nr_prod):
        p = CoffeeFactory('Factory', i, distributor)
        threads.append(Thread(target=p.process))

    for i in range(nr_con):
        c = User('Consumer', i, distributor)
        threads.append(Thread(target=c.process))

    # starts the threads
    for t in threads:
        t.start()

    # waiting for the threads to finish
    for t in threads:
        t.join()


if __name__ == '__main__':
    main()
