# Node.prev is not working right now.

class Node:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty.")
            return
        itr = self.head
        while itr:
            print(itr.data + "\n")
            itr = itr.next
    
    def insert_at_beginning(self,data):
        node = Node(data, None, self.head)
        self.head = node
    
    def insert_at_end(self,data):
        if self.head is None:
            node = Node(data, None, self.head)
            self.head = node
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data)

    def get_lenght(self):
        ln = 0
        itr = self.head
        while itr:
            ln += 1
            itr = itr.next
        
        return ln

    def insert_at(self, data, index = int):
        if index < 0 or type(index) != int or index >= self.get_lenght():
            raise Exception("Invalid index.")
        
        if index == 0:
            self.insert_at_beginning(data)

        count = 0
        itr = self.head
        while itr:
            if count == (index - 1):
                node = Node(data, None, itr.next)
                itr.next = node

            count += 1
            itr = itr.next

    def remove_at(self, index = int):
        if index < 0 or type(index) != int or index >= self.get_lenght():
            raise Exception("Invalid index.")
        
        if index == 0:
            self.head = self.head.next

        count = 0
        itr = self.head
        while itr:
            if count == (index - 1):
                itr.next = itr.next.next
                break

            count += 1
            itr = itr.next

    def insert_values(self, data):
        for value in data:
            self.insert_at_end(value)

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        count = 0
        while itr:
            count += 1
            if itr.data == data_after:
                self.insert_at(data_to_insert, count)
                return
            
            itr = itr.next

    def remove_by_value(self, data):
        itr = self.head
        
        while itr:
            try:
                if itr.data == data:
                    self.head = itr.next
                    break

                elif itr.next.data == data:
                    itr.next = itr.next.next
                    break

                itr = itr.next
            except:
                print(f"There is no {data}")
                break


# if __name__ == "__main__":
#     lst = LinkedList()
#     lst.insert_at_beginning("value1")
#     lst.insert_at_beginning("value2")
#     lst.insert_at_beginning("value3")
#     lst.insert_at_end("value0")
#     lst.print()
#     print(lst.get_lenght())

#     lst.insert_at("valueInserted", 2)
#     lst.print()
#     print(lst.get_lenght())

#     lst.remove_at(2)
#     lst.print()
#     print(lst.get_lenght())

#     lst.insert_values(["banana","mango","grapes","orange"])
#     lst.print()
#     print(lst.get_lenght())

#     lst.insert_after_value("banana", "bananaNumber2")
#     lst.print()
#     print(lst.get_lenght())

#     lst.remove_by_value("banana")
#     lst.print()
#     print(lst.get_lenght()) 


# """ if __name__ == "__main__":
#     ll = LinkedList()
#     ll.insert_values(["banana","mango","grapes","orange"])
#     ll.print()
#     print("----------")
#     ll.insert_after_value("mango","apple")
#     ll.print()
#     print("----------")
#     ll.remove_by_value("orange")
#     ll.print()
#     print("----------")
#     ll.remove_by_value("figs")
#     ll.print()
#     print("----------")
#     ll.remove_by_value("banana")
#     print("1")
#     ll.remove_by_value("mango")
#     print("1")
#     ll.remove_by_value("apple")
#     print("1")
#     ll.remove_by_value("grapes")
#     print("1")
#     ll.print()
#     print("----------") """
