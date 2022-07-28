class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.down = None
        self.up = None
        self.back = None
        self.flatten = []

    def print_linkedlist(self, head):
        temp = head
        while temp:
            self.flatten.append(temp.data)
            print(temp.data, end=' ')

            if temp.down != None:
                self.print_down(temp.down)
            if temp.up != None:
                self.print_down(temp.up)
            temp = temp.next

    def print_down(self, head):
        temp = head
        while temp:
            self.flatten.append(temp.data)
            print(temp.data, end=' ')
            if temp.back != None:
                self.print_back(temp.back)
            if temp.next != None:
                self.print_back(temp.next)
            temp = temp.down

        return

    def print_up(self, head):
        temp = head
        while temp:
            self.flatten.append(temp.data)
            print(temp.data, end=' ')
            temp = temp.up

        return

    def print_back(self, head):
        temp = head
        while temp:
            self.flatten.append(temp.data)
            print(temp.data, end=' ')
            temp = temp.back

        return

    def print_N_Sort_flatten(self):
        temp = len(self.flatten)
        swapped = False

        for i in range(temp - 1):
            for j in range(0, temp - i - 1):
                if self.flatten[j] > self.flatten[j + 1]:
                    swapped = True
                    self.flatten[j], self.flatten[j + 1] = self.flatten[j + 1], self.flatten[j]
        if not swapped:
            return

        temp = self.flatten
        for x in temp:
            print(x, end=' ')


node_1 = Node(10)
node_2 = Node(1)
node_3 = Node(8)
node_4 = Node(6)
node_5 = Node(2)
node_6 = Node(3)
node_7 = Node(7)
node_8 = Node(4)
node_9 = Node(5)
node_10 = Node(9)

node_1.next = node_2
node_2.down = node_3
node_3.down = node_4
node_4.back = node_5

node_2.next = node_6

node_6.next = node_10
node_6.up = node_7
node_6.down = node_8
node_8.next = node_9

print("Linked List")
node_1.print_linkedlist(node_1)
print("\nSorted linked list")
node_1.print_N_Sort_flatten()