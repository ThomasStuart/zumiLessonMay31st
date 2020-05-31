def isQuitKeyword( string ):
    # try to determine if the string contains a Q, neglecting capitalizations and spaces 
    for i in range(0, len(string)):
        if( string[i] == 'q' or string[i] == 'Q'):
            return True 
    return False

def load_route( dictionary ):
    routes         = [] #this will hold a queue of routes we enter
    lettersEntered = []
    
    #Ask the user how many routes they want to input ? 
    numRoutes =  input("Enter number of routes you want to run in Graph:  ")
    numRoutes =  int(numRoutes) #converts string value to integer 
    
    # Displays the valid vertices in the graph 
    print("Vertices: [ ", end='')
    # first print all the keys = letters out to the console 
    for key in dictionary:
        print(key, end=', ')
    print("]")
    
    # prompt the user to enter a startNode
    startVertex = input("Input a starting Vertex:  ")
    
    while startVertex not in dictionary:
        print("You entered an INVALID vertex ")
        startVertex = input("Input a starting Vertex again:  ")
    
    # print what the user entered
    print(startVertex)
    
    # prompt the user to enter a endNode 
    endVertex = input("Input a ending Vertex:  ")
    
    while endVertex not in dictionary:
        print("You entered an INVALID vertex ")
        endVertex = input("Input a end Vertex again:  ")
    
    # print what the user entered
    print( endVertex )
    
    
    #routes.append( G.search(startVertex, endVertex)  ) # First route was added to the routes container 
    
    for i in range(0, numRoutes-1):
        startVertex = endVertex
        print("Route #", len(routes)+1 )
        endVertex = input("\t Next Vertex: ")   
        
        if isQuitKeyword(endVertex):
            print("Exited Early beacause of quit Keyword 'Q' or 'q' ")
            break
        
        print("Entered route, from ", startVertex , " to ", endVertex)
        #routes.append( G.search(startVertex, endVertex) )
        
    
    print("total Num of t", len(routes))
    return routes

dictionary1 = {'s':1, 'x':2, 'a':3, 'b':4}
load_route(dictionary1)
