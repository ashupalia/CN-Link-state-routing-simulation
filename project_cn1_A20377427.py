
# coding: utf-8

# In[1]:

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~CS542-04 - Project~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#Link State Routing Algorithm

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Importing the libraries~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
import os
import sys
import os
import os.path
import heapq

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Printing the choices available ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

print("Select one option from below: \n")
print("1. Press 1 for creating the network topology")
print("2. Press 2 for building the connection table")
print("3. Press 3 for finding the shortest path to destination")
print("4. Press 4 to modify the topology")
print("5. Press 5 for finding the best router for broadcast ")
print("6. Press 6 to exit the program")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Declaring the variables ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

node_edge = list()
dictionary_values= dict()
graphical_representaion = list()
nodestot = 0
a = 0
nodes_dict = dict()
notVisited = dict()
rajwada = dict()
newpon = list()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#~~~~~~~~~~~~~~~~~~~~ Initializing the program by creating a constructior~~~~~~~~~~~~~~~~~~~#

def __init__(self):
    self.grah = list()
    self.cst_dict = {}
    self.vetex = []
    self.lininterface = []
    self.pth = list()
    self.unSen = {} #doubtful
    self.prvNode = {}
    self.senNode = {}
    self.qwdqw = {}
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#~~~~~~~~~~~~~~The following functions, are for exception cases to raise the error ~~~~~~~~~~~~~~#

def errhandler():
    
    print("The input is not a valid input, Enter an integer value between 1-6.\n")
    command = input("Please Enter the command: \n")
    takeaction.get(command, errhandler)()
    
def err1handler():
    takeaction = {"1" : doCaseOne, "6" : doCaseSix}
    print("The input is not a valid input, Enter 1 for taking the input file, or enter 6 to exit\n")
    command = input("Please Enter the command: \n")
    takeaction.get(command, err1handler)()
    
def erronehandler():
    takeaction = {"2" : doCasetwo, "5" : doCaseFivepointone,"6" : doCaseSix}
    print("The input is not a valid input, Enter 2 for the source router, or enter 5 to see the best router or enter 6 to exit\n")
    command = input("Please Enter the command: \n")
    takeaction.get(command, erronehandler)()
    
def errtwohandler():
    takeaction = {"3" : doCaseThree, "5" : doCaseFivepointone, "6" : doCaseSix}
    command = input("Please Enter the command, Enter 3, to find shortest path to destination or 5, to see the best router or 6 to exit the program: \n")
    takeaction.get(command, errtwohandler)()
    
def errS3handler():
    takeaction = {"4" : doCaseFour, "5" : doCaseFivepointone, "6" : doCaseSix}
    print("The input is not a valid input, Enter an integer value between 4-6.")
    command = input("Please Enter the command: \n")
    takeaction.get(command, errS3handler)()
    
def err5handler():
    takeaction = {"5" : doCaseFivepointtwo, "6" : doCaseSix}
    print("Press 5 to see the best router, with modifying the updates on router or press 6 to exit")
    command = input("Please Enter the command: \n")
    takeaction.get(command, err5handler)()
    
def errexithandler():
    takeaction = {"5": doCaseFivepointone, "6" : doCaseSix}
    command = input("Not many choices, press 6 and exit: \n")
    takeaction.get(command,errexithandler())
    
def errexhandler():
    takeaction = {"6" : doCaseSix, "7" : "Please press 6 and exit"}
    command = input("Not n*n matrix, press 6 and exit and import a correct n*n file: \n")
    takeaction.get(command,errexhandler())
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#~~~~~~~~~~~~~This is the implementation of the dijkstra algorithm to find the shortest path ~~~~~~~~~~~~~~~#


    
def dijkstra(start):
    global dictionary_values
    global notVisited
    global nodeBefore
    global visitedNode
    global nodes_dict
    #creates a new dictionary with key as the routers and values as infinite.
    notVisited = {node: float('inf') for node in node_edge}
    visitedNode = dict()
    nodeBefore = dict()
    newnod = list()
    startingNode = start
    raju = dict()
    nodewa = list()
    initialDist = 0
    #creates a new dict with all the routers as key and an empty list as the value
    nodes_dict = {node: [] for node in node_edge}
    notVisited[startingNode] = initialDist
    while len(notVisited) > 0:
        for key, value in dictionary_values[startingNode].items():
            if key not in notVisited:
                continue
            newDistance = initialDist + value
            if newDistance < notVisited.get(key, float('inf')):
                notVisited[key] = newDistance
                nodeBefore[key] = startingNode
                if not nodes_dict[startingNode]:
                    nodes_dict[key] = [key]
                else:
                    nodes_dict[key] = list(nodes_dict[startingNode])
        visitedNode[startingNode] = initialDist
        del notVisited[startingNode]
        if not notVisited:
            break
        currentStatus = [node for node in notVisited.items() if node[1]]
        #returns the distance from the current node or the starting node to all other nodes in the topology
        startingNode, initialDist = sorted(currentStatus, key=lambda x: x[1])[0]


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#~~~~~~~~~~~~doCaseOne takes the input file and create a matrix if the input file is a valid file~~~~~~~~#
def doCaseOne():
    global q
    global graphical_representaion
    #takes the input file in .txt format only.
    kyuk = list()
    noti = dict()
    print("Enter the input file in a text format - .txt \n")
    file = input()
    #file should not be empty and it should exist in the folder. 
    if file.endswith('.txt') and os.path.isfile(file) and os.stat(file).st_size != 0:
        print("The Network topology is : \n")
        fo = open(file)
        #extracting the data from the input file and creating a list of list.
        graphical_representaion = [list(map(int, x.split())) for x in fo]
        #prints the data in the form of a matrix
        for line in graphical_representaion:
            for item in line:
                print(item, end='    ')
            print()
        #checks the length of the matrix or the rows   
        rows = len(graphical_representaion)
        count = 0
        #checks the columns of the matrix
        for row in graphical_representaion:
            column_len = len(row)
        #The matrix should be of the form n*n matrix.    
        if column_len == rows:
            print("The input file is a n*n matrix\n ")
            nodestot=len(graphical_representaion)
            #The number of rows or the number of routers in the network.
            print("\nTotal number of nodes present in the given topology: ", len(graphical_representaion))
            #It creats a dictionary of the graph, the dictionary is of the form {1,{2,3}}.
            #this will be later used in calculating the path using the path finding function.
            for i in range(len(graphical_representaion)):
                mat = dict()
                raj = list()
                for j in range(len(graphical_representaion)):
                    if i != j and graphical_representaion[i][j] != -1:
                        mat[j + 1] = graphical_representaion[i][j]
                dictionary_values[i + 1] = mat
                node_edge.append(i + 1)
                q = len(dictionary_values)
        #The input text file is not of the form n*m.
        #It will Exit the sytem by displaying the message.
        else:
            print("It is not a n*n matrix\n")
            print("Import a n*n matrix file agin by running the program again\n")
            while True:
                raise SystemExit
            
            

    #input file is not a text file or an empty file or dosenot exist.
    else: 
        print("Enter the input file again, as the file entered is not a valid one.")
        takeaction = {"1" : doCaseOne, "6" : doCaseSix}
        command = input("Please, Enter the command, press 1 or 6 \n")
        takeaction.get(command, err1handler)()
    #Once the caseOne is done, the choice available will be 2,5,6
    takeaction = {"2" : doCasetwo,  "5" : doCaseFivepointone, "6" : doCaseSix}
    command = input("Please, Enter the command, options are 2 or 5 or 6: \n")
    takeaction.get(command,erronehandler)() 
    
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#~~~~~~~~~~~~~~~~~~~~~~~~~doCasetwo finds the interface to all the destination~~~~~~~~~~~~~~~~~~~~~~~~~~~#    
def doCasetwo():
    global a
    global q
    nonu = list()
    rajj = 0
    notd = dict()
    #Just a print statement
    print("\nPlease, select a source router. It should be an integer value")
    #Checks if the input is valid or not. 
    #Input should always be an integer value
    while True:
        try:
            start = int(input("Please Enter an integer value, Do not enter any negative value or an invalid input"))
        except ValueError:
            print("Not an integer! Please enter a valid router ID")
            continue
        else:
            break
    q = len(dictionary_values)
    #The input for source router should be a valid router.
    #By valid, it means the router should be present in the network topology.
    #no negative integer accepted.
    if start > q or start < 1:
        print("Not a valid router!")
        takeaction = {"2" : doCasetwo,  "5" : doCaseFivepointone, "6" : doCaseSix}
        command = input("Please Enter the command 2 or 5 or 6: \n")
        takeaction.get(command,erronehandler)() 
    a = start
    #calling path finding function with the parameter as the input taken.
    dijkstra(start)
    print("\nThe connection table for router is")
    print("\n\tDestination \tInterface")
    print("==================================")
    for key in nodes_dict:
        print("\t",key, "\t\t", nodes_dict[key])
    
    #once casetwo is finished, the available options are 3, 5, 6
    takeaction = {"3" : doCaseThree, "5" : doCaseFivepointone, "6" : doCaseSix}
    command = input("Please Enter the command, options are 3,5,6: \n")
    takeaction.get(command, errtwohandler)()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#~~~~~~~~~~~~doCaseThree finds the shortest path and the cost to the destination from the source~~~~~~~~~~#
def doCaseThree():
    global a
    global q
    global destination
    destu = list()
    dicta = dict()
    nop = list()
    
    print("\nSelect the destination router to find the shortes path from Source to Destnation:\n")
    #it checks the input, it should be an integer
    while True:
            try:
                destination = int(input("Please enter a valid router and an integer value \n"))
            except ValueError:
                print("Not an integer! Please enter a valid router ID")
                continue
            else:
                break
    #the input should be an existing router.
    q = len(dictionary_values)
    if destination < 1 or destination > q:
        print("Enter a valid router again by pressing the command 3")
        takeaction = {"3" : doCaseThree,  "5" : doCaseFivepointone, "6" : doCaseSix}
        command = input("Please Enter the command, choices -> 3 or 5 or 6: \n")
        takeaction.get(command,errtwohandler)()    
    #Finding the minimum cost to the destination.
    destination1 = destination
    b = destination
    c = visitedNode[destination]
    print("\nThe minimum cost from the source %s to the detination %s is equal to %s" % (a,b,c))
    #Finding the shortest path to the destination.
    path = list()
    while 1:
        path.append(destination)
        if destination == a:
            break
        destination = nodeBefore[destination]
    path.reverse()

    destination = destination1
    print("\nThe shortest Path from the source %s to the detination %s is equal to %s"%(a,b,path))
   
    #Once case3 is done, the available options are 4,5,6
    takeaction = {"4" : doCaseFour, "5" : doCaseFivepointone, "6" : doCaseSix}
    command = input("Please Enter the command: \n")
    takeaction.get(command, errS3handler)()
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#~~~~~~~~~~~~~~~~~~~doCaseFour modifies the network topology by deleting tyhe router~~~~~~~~~~~~~~~~~~~~~#    
def doCaseFour():
    global notVisited
    global a
    global destination
    global q
    global newlis
    
    qrt = list()
    newton = 0
    rajton = 0
    
    print("\nPlease, select a Router to be Removed.")
    #the input should be an integer
    while True:
            try:
                down_router = int(input("Please enter a valid router - an integer value\n"))
            except ValueError:
                print("Not an integer! Please enter a valid router ID")
                continue
            else:
                break
    #The router should be a valid and existing router.
    q = len(dictionary_values)
    if down_router < 1 or down_router > q:
        print("Enter valid Router")
        takeaction = {"4" : doCaseFour,  "5" : doCaseFivepointone, "6" : doCaseSix}
        command = input("Please Enter the command, choice -> 4 or 5 or 6: \n")
        takeaction.get(command,errS3handler)()
        
    #downs the router 
    downminusone = down_router - 1
    for i in range(len(graphical_representaion)):
        matrix = {}
        for j in range(len(graphical_representaion)):
            if i != j != downminusone and i != j and graphical_representaion[i][j] != -1:
                matrix[j + 1] = graphical_representaion[i][j]

        dictionary_values[i + 1] = matrix
    del dictionary_values[down_router]
    del node_edge[downminusone]
    #a case if deleting router was the start node. We will perform doSteptwo again.
    if down_router == a:
        while True:
            try:
                a = int(input("Enter new start node again as removed node was the start node \n"))
            except ValueError:
                print("Not an integer! Enter a valid router ID")
            
            else:
                break
                
    dijkstra(a)

    print("\nRouter %s Connection Table:" % a)
    print("\n\tDestination \tInterface")
    print("==================================")
    for key in nodes_dict:
        print(key, "\t\t", nodes_dict[key])
    #if the deleted node is the destination node.
    path = []
    destination2 = destination
    if down_router == destination:
        
        
        print("\nSelect the destination router:")

        while True:
            try:
                destination = int(input("Enter a new destination node again as removed node was the destination node \n"))
                destination2 = destination
            except ValueError:
                print("Not an integer! Enter a valid router ID")
            
            else:
                break        
    while 1:
        path.append(destination)
        if destination == a:
            break
        destination = nodeBefore[destination]
    path.reverse()
    destination = destination2
    
    print("The new shortest distance to destination is ",visitedNode[destination])
    print("The new shortest path is ",path)
    newlis = list()
    #available options
    for key,value in dictionary_values.items():
        newlis.append(key)
    takeaction = {"5" : doCaseFivepointtwo, "6" : doCaseSix}
    command = input("Please Enter the command: \n")
    takeaction.get(command, err5handler)()
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#~~~~~~~~~~~~~~doCaseFivepointone displays the best broadcasting router in the network topology~~~~~~~~~~~~~~~# 
def doCaseFivepointone():
    global graphical_representaion
    global newlis
    
    
    bishtwa = dict()
    lishtwa = list()
    for a in range(len(graphical_representaion)):
        dijkstra(a + 1)
        count = 0
        for key, val in visitedNode.items():
            count = count + val
        
        print("\t",a + 1,"\t\t", count)

        lishtwa.append(count)
        
    u = min(lishtwa)
    v = lishtwa.index(u)
    vplusone = v + 1
    r = u
    print("\nBest Router for broadcsting before modifying the topology is %s with lowest cost of %s" % (vplusone, min(lishtwa)))
    
    takeaction = { "2" : doCasetwo, "5" : doCaseFivepointone, "6" : doCaseSix}
    command = input("Please Enter the command: \n")
    takeaction.get(command, erronehandler)()
    
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#~doCaseFivepointtwo displays the best broadcasting router in the network topology, if there is a modification in the router~~~#     
    
def doCaseFivepointtwo():
    global graphical_representaion
    global newlis
    
    lisht = list()
    bistu = dict()
    bisht = 0
    lest = list()
    for a in newlis:
        dijkstra(a)
        count = 0
        for key,val in visitedNode.items():                
            count = count + val
        print("\t",a,"\t\t",count)
        lisht.append(count)
        lest.append(a)


    u = min(lisht)
    v = lisht.index(u)
    t = lest[v]

    print("\nBest Router for broadcasting after modifying the topology is %s with lowest cost of %s"%(t,u))
    
    takeaction = {"5": doCaseFivepointtwo, "6" : doCaseSix}
    command = input("Please Enter the command: \n")
    takeaction.get(command, errexithandler)()
    
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Exits the program~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#       
def doCaseSix():
    print("\nExiting...")
    exit()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Main ofthe program~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#      

def main():
    takeaction = {"1" : doCaseOne, "6" : doCaseSix}
    command = input("Please Enter the command: \n")
    takeaction.get(command, err1handler)()
    
if __name__ == '__main__':
    main()
    




# In[ ]:



