class Node:
    def __init__(self, Data):
        self.data = Data
        self.next = None


    def SumOfLastN_Nodes(self,x, n):
        temp = self

        while temp:
            if temp.data == x:
                while temp.next:

                    print(temp.next.data)
                    t.append(temp.next.data)

                    temp = temp.next

            temp = temp.next
        total = 0
        for i in range(0, len(t)):
            total = total + t[i]
        print(total)
        return
t = []

node_1 = Node(5)
node_2 = Node(10)
node_3 = Node(6)
node_4 = Node(4)
node_5 = Node(1)
node_6 = Node(12)

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5
node_5.next = node_6


n = '6'

node_1.SumOfLastN_Nodes(6, n)
