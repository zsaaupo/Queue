"""
Queue
"""
print(__doc__)




class Queue():


    def __init__(self, queue):

        self.queue = queue


    def enqueue(self, value):

        if len(self.queue) < 5:
            self.queue.append(value)

        else:
            print("Queue is full")
            return "Queue is full"


    def dequeue(self):

        if len(self.queue) == 0:
            print("Queue is Empty")
            return "Queue is empty"

        else:
            self.queue.pop(0)
    

    def is_empty(self):

        if len(self.queue) == 0:
            return True

        else:
            return False


    def is_full(self):

        if len(self.queue) == 5:
            return True

        else:
            return False




obj_01 = Queue([])

obj_01.enqueue("a")
obj_01.enqueue("b")
obj_01.enqueue("c")
obj_01.enqueue("d")
obj_01.enqueue("e")
obj_01.enqueue("f")

print("after enqueue", obj_01.queue)

print("checking if queue is full =", obj_01.is_full())

obj_01.dequeue()
obj_01.dequeue()
obj_01.dequeue()
obj_01.dequeue()
obj_01.dequeue()
obj_01.dequeue()

print("after dequeue", obj_01.queue)

print("checking if queue is empty =", obj_01.is_empty())
