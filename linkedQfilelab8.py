class Node:

    def __init__(self, value, next = None):
        self.value = value  # t.ex. "A"
        self.next = next  # -->class Node(LinkedQ):


class LinkedQ:
    #q=LinkedQ så q skapar första och sista noden
    def __init__(self):
        #self.linked = linked
        self.__first = None   # __ = privat attribut
        self.__last = None


    def enqueue(self, new):
        x = Node(new)
        if self.__first == None:  # if empty queue
            self.__first = x
            self.__last = x
        else:
            self.__last.next = x   # x is added to linked list
            self.__last = x        #last pointer goes to x

    def dequeue(self):
        x = self.__first.value
        self.__first = self.__first.next #sätter nästa nod som första nod eftersom vi plockar bort den första
        return x

    #kollar om det är tomt eftersom den enbart returnerar om self.first är == None
    def is_empty(self):
        return self.__first == None

    def peek(self):
        """visar översta objektet utan att ta bort det"""
        if self.__first is not None:
            return self.__first.value
