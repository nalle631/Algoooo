class LinkedGraph:
    def __init__(self, n):
        self.n = n
        self.nodeArr = []

        #
        
        
        #self.countEdge = 0

        i = 0
        while(i < n):
            #print(self.nodeArr)
            self.nodeArr.append(LinkedList())
            i = i + 1
    
    def addWeight(self, frm, to, weight):
        
        if(weight < 0 or frm == to or frm > self.n or to > self.n):
            raise Exception
        currentLL = self.nodeArr[frm]
        currentLL.insertEdge(to, weight)

        currentLL = self.nodeArr[to]
        currentLL.insertEdge(frm, weight)
        #self.countEdge = self.countEdge + 1
        # big lips
        #self.addWeight(to, frm, weight)

    def getEdge(self, node):
        currentLL = self.nodeArr[node]
        currentLL.searchEdge(node)

    def check(self,node):
        visited = [False] * self.n
        queue = []
        queue.append(node)
        visited[node] = True
        
        while(queue):
            value = queue.pop(-1)
            print(self.nodeArr[value].curTrav.node)
            while(self.nodeArr[value].curTrav != None):
                i = self.nodeArr[value].curTrav.node
                if(visited[i] == False):
                    queue.append(i)
                    visited[i] = True
        print(visited)
            # for x in self.nodeArr[value]:
            #     print(visited)
            #     if visited[x.head.next.node] == False:
            #         queue.append(x.head.next.node)
            #         visited[x.head.next.node] = True
        # for y in self.visited:
        #     if y == False:
        #         return False
        # return True
           
        # check = True    
        # for x in self.nodeArr:
        #     if x.head.next == None:
        #         check = False
        #         return check
        # return check

class LinkedList:
    def __init__(self, head = None):
        
        self.head = head
        self.size = 0
        self.curTrav = None
 
    def insertEdge(self, to, weight):
        
        newNode = Node(to , weight,  self.head)
        self.head = newNode
        self.curTrav = newNode
        

        self.size = self.size + 1

        
    def traverse(self, i):
         self.curTrav = self.curTrav.next
        

    def searchEdge(self,node):
        if self.head == None:
            raise Exception
        currentSearch = self.head
        i = 0
        while(i < self.size):
            print(node , " is connected to ",currentSearch.getNode(), currentSearch.getWeight())
            currentSearch = currentSearch.next
            i = i + 1
            

    def getHead(self):
        return self.head

class Node:
    def __init__(self, node, weight, next):
        self.node = node
        self.weight = weight
        self.next = next

    def getNode(self):
        return self.node

    def getWeight(self):
        return self.weight
 

link = LinkedGraph(5)

link.addWeight(0,1,10)
link.addWeight(1,2,10)
link.addWeight(2,3,11)
link.addWeight(3,4,8)

link.getEdge(0)
link.getEdge(1)
link.getEdge(2)
link.getEdge(3)
link.getEdge(4)
link.check(2)

