"""
    Basic thread handling exercise:

    Use the Thread class to create and run more than 10 threads which print their name and a random
    number they receive as argument. The number of threads must be received from the command line.

    e.g. Hello, I'm Thread-96 and I received the number 42

"""

import sys
import random
import threading


# print function for every thread
def my_thread(number):
    print("Hello, I'm %s and I received the number %d"
          % (threading.currentThread().getName(), number))


def main():
    if len(sys.argv) != 2:
        print("Wrong number of arguments")
        print("Please insert the number of threads")
        sys.exit()

    num_threads = int(sys.argv[1])
    threads = [threading.Thread(target=my_thread,
                                args=(random.randint(0, 100),))
               for i in range(num_threads)]

    # starting the threads
    for thread in threads:
        thread.start()

    # waiting for the threads to finish
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
