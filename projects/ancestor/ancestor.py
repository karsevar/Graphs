
def earliest_ancestor(ancestors, starting_node):
    
    # first create the graph in which the relationships 
    # between parent and child can be inferred.

    # input data structure (parent, child)
    # the graph will be directed because ancestry 
    # can only go in one direction which is 
    # child -> parent -> grand parent -> so on 

    # first populate a graphs data structure with 
    # the nodes and the edges from the ancestors 
    # input data 

    graph = {}

    for pair in ancestors:
        parent = pair[0]
        child = pair[1] 

        if child not in graph:
            graph[child] = set()
            graph[child].add(parent) 

        else:
            graph[child].add(parent)

    for pair in ancestors:
        parent = pair[0]
        
        if parent not in graph:
            graph[parent] = set() 

    # print(graph)
    # the graph is now only going one way from child to parent.
    # there are some parents that don't have a key in the dictionary 
    # this can be used to terminate the search 

    # For this solution I will use breadth first search with 
    # some modifications:
        # first a path will be returned back once a node is found 
        # that doesn't have any neighbors 

        # second a loop will be created to go through the neighbors 
        # of each node (much like basic breadth first search)

    ## plan:
    # edge cases:
    # if the starting node does not have any neighbors return 
    # -1 

    # else:
        # create an array that will hold all the ancestor routes
        # create a queue 
        # initialize the queue with the starting_node 
        # create a visited set
        # while the queue is not empty:
            # dequeue the head of the queue:
            # if current node is not in visited set:
                # if current_node does not have any neighbors 
                    # append the path to the routes array 
                # if not:
                    # for loop through the neighbors and 
                    # enqueue each neighbor in the queue

    if len(graph[starting_node]) == 0:
        return -1




test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 2))