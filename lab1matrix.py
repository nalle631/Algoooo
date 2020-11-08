class Graph:
    def __init__(self, n):
        self.matrix = []
        
        i = 0
        while (i < n):
            j = 0
            tempMatrix = []
            while(j < n):
                tempMatrix.append(0)
                j = j + 1
            self.matrix.append(tempMatrix)
            i = i + 1

    def addEdge(self,frm,to,weight):
        frm = frm - 1
        to = to - 1
        if(weight < 0) or frm == to or frm >= len(self.matrix) or to >= len(self.matrix):
            raise Exception
        self.matrix[frm][to]=weight
        self.matrix[to][frm]=weight

    def checkEdge(self,node):
        node = node - 1
        if (len(self.matrix) < node):
            raise Exception
        i = 0
        for weight in self.matrix[node]:
            if(weight != 0):
                print(node+1, " is connected with ", i+1, " with weight ", weight)
            i = i + 1

    def print(self):
        print(self.matrix)

myg = Graph(5)

myg.addEdge(1,2,6)
myg.addEdge(1,4,7)
myg.checkEdge(1)

myg.addEdge(2,3,5)
myg.addEdge(2,4,8)
myg.addEdge(2,5,4)
myg.checkEdge(2)

myg.addEdge(3,4,3)
myg.addEdge(3,5,7)
myg.checkEdge(3)

myg.addEdge(4,5,9)
myg.checkEdge(4)

myg.checkEdge(5)

myg.print()


