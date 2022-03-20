from ast import arg
from Queue import Queue
from threading import Thread
import time

orders = Queue()
def place_order(items):
    for order in items:
        print (f"Placing order...{order}")
        orders.enqueue(order)
        time.sleep(0.5)

def serve():
    while True:
        try:
            served = orders.dequeue()
        except IndexError:
            print ("No more orders")
            break
        print (f"Order served: {served}")
        time.sleep(2)

items = ("pizza", "samosa", "pasta", "mutter panner", "handva", "dhokla")
place_order_thread = Thread(target=place_order, args=(items, ))
server_thread = Thread(target=serve)

place_order_thread.start()
time.sleep(1)
server_thread.start()